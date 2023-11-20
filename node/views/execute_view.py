from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute
from uc_flow_schemas.flow import RunState
import httpx
import asyncio
import logging


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            action = json.node.data.properties.get('action')
            if action == 'authorization':
                hostname = json.node.data.properties.get('hostname')
                email = json.node.data.properties.get('email')
                branch = json.node.data.properties.get('branch')
                api_key = json.node.data.properties.get('api_key')
                auth_url = f'https://{hostname}/v2api/auth/login'
                auth_data = {'email': email, 'api_key': api_key}
                async with httpx.AsyncClient() as client:
                    response = await client.post(auth_url, json=auth_data)
                    response.raise_for_status()
                    auth_result = response.json()
                    token = auth_result.get('token')
                    if token:
                        json.get_session().token = token
                    else:
                        logging.warning("Token not found in the auth result.")
                    auth_data_to_save = {'auth_result': auth_result}
                    await json.save_results(
                        [auth_data_to_save], output_handle='authorization_data'
                    )

            elif action == 'customer' and hasattr(json.get_session(), 'token'):
                resource = json.node.data.properties.get('resource')
                operation = json.node.data.properties.get('operation')
                if resource == 'customer':
                    if operation == 'index':
                        parameters = json.node.data.properties.get(
                            'parameters', []
                        )
                        id_filter = next(
                            (
                                param['id']
                                for param in parameters
                                if param['name'] == 'id'
                            ),
                            None,
                        )
                        is_study_filter = next(
                            (
                                param['is_study']
                                for param in parameters
                                if param['name'] == 'is_study'
                            ),
                            None,
                        )
                        name_filter = next(
                            (
                                param['name']
                                for param in parameters
                                if param['name'] == 'name'
                            ),
                            None,
                        )
                        lead_status_id_filter = next(
                            (
                                param['lead_status_id']
                                for param in parameters
                                if param['name'] == 'lead_status_id'
                            ),
                            None,
                        )
                        page_filter = next(
                            (
                                param['page']
                                for param in parameters
                                if param['name'] == 'page'
                            ),
                            None,
                        )
                        customer_url = f'https://{hostname}/v2api/customer'
                        headers = {'X-ALFACRM-TOKEN': json.get_session().token}
                        params = {
                            'id': id_filter,
                            'is_study': is_study_filter,
                            'name': name_filter,
                            'lead_status_id': lead_status_id_filter,
                            'page': page_filter,
                        }
                        async with httpx.AsyncClient() as client:
                            response = await client.get(
                                customer_url, headers=headers, params=params
                            )
                            response.raise_for_status()
                            customer_list = response.json()
                        try:
                            customer_data_to_save = {
                                'customer_list': customer_list
                            }
                            await json.save_results(
                                [customer_data_to_save],
                                output_handle='customer_data',
                            )
                        except Exception as e:
                            await json.save_error(f"Error saving results: {e}")
                            json.state = RunState.error
                        await asyncio.sleep(5)
                        try:
                            saved_result = await json.get_result(
                                "customer_data"
                            )
                        except Exception as e:
                            await json.save_error(
                                f"Error getting saved result: {e}"
                            )
                            json.state = RunState.error
                    elif operation == 'create':
                        customer_properties = json.node.data.properties.get(
                            'customer_properties', {}
                        )
                        create_customer_url = (
                            f'https://{hostname}/v2api/customer'
                        )
                        headers = {'X-ALFACRM-TOKEN': json.get_session().token}
                        async with httpx.AsyncClient() as client:
                            response = await client.post(
                                create_customer_url,
                                headers=headers,
                                json=customer_properties,
                            )
                            response.raise_for_status()
                            created_customer = response.json()
                        try:
                            created_customer_data_to_save = {
                                'created_customer': created_customer
                            }
                            await json.save_results(
                                [created_customer_data_to_save],
                                output_handle='created_customer_data',
                            )
                        except Exception as e:
                            await json.save_error(
                                f"Error saving creation results: {e}"
                            )
                            json.state = RunState.error
                    elif operation == 'update':
                        customer_id = json.node.data.properties.get(
                            'customer_id'
                        )
                        updated_properties = json.node.data.properties.get(
                            'updated_properties', {}
                        )
                        update_customer_url = (
                            f'https://{hostname}/v2api/customer/{customer_id}'
                        )
                        headers = {'X-ALFACRM-TOKEN': json.get_session().token}
                        async with httpx.AsyncClient() as client:
                            response = await client.patch(
                                update_customer_url,
                                headers=headers,
                                json=updated_properties,
                            )
                            response.raise_for_status()
                            updated_customer = response.json()
                        try:
                            updated_customer_data_to_save = {
                                'updated_customer': updated_customer
                            }
                            await json.save_results(
                                [updated_customer_data_to_save],
                                output_handle='updated_customer_data',
                            )
                        except Exception as e:
                            await json.save_error(
                                f"Error saving update results: {e}"
                            )
                            json.state = RunState.error
        except httpx.RequestError as e:
            error_message = f'HTTP request failed: {e}'
            logging.exception(error_message)
            await json.save_error(error_message)
            json.state = RunState.error
        except Exception as e:
            error_message = f'Error: {e}'
            logging.exception(error_message)
            await json.save_error(error_message)
            json.state = RunState.error
        return json
