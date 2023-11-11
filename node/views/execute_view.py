from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.views import execute
from uc_flow_schemas.flow import RunState


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            switch_field = json.node.data.properties.switch_field
            if switch_field:
                value_1 = json.node.data.properties.value_1
                value_2 = json.node.data.properties.value_2
                result = f"Переключатель включен. Значение 1: {value_1}, Значение 2: {value_2}"
                await json.save_result({"result": result})
            else:
                await json.save_result(
                    {
                        "result": "Переключатель выключен. Нет данных для отображения."
                    }
                )
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json
