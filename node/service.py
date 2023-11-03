import ujson
from typing import List, Tuple

from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService
from uc_flow_nodes.views import info, execute
from uc_flow_schemas import flow
from uc_flow_schemas.flow import Property, CredentialProtocol, RunState
from uc_http_requester.requester import Request


class NodeType(flow.NodeType):
    id: str = 'fe19a64a-c274-412d-a6e8-66b9639e1f3a'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'GoogleExtension'
    displayName: str = 'GoogleExtension'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    description: str = 'GoogleExtension'
    properties: List[Property] = [
        Property(
            displayName='Текстовое поле',
            name='text_field',
            type=Property.Type.STRING,
            placeholder='Введите текст',
            description='Текстовое поле для ввода данных',
            required=True,
            default='Test data',
        ),
        Property(
            displayName='Числовое поле',
            name='number_field',
            type=Property.Type.NUMBER,
            placeholder='Введите число',
            description='Числовое поле для ввода данных',
            required=True,
            default=0,
        ),
        Property(
            displayName='Переключатель',
            name='field_type',
            type=Property.Type.BOOLEAN,
            placeholder='Выберите тип поля',
            description='Выберите тип поля: если включено, текстовое поле '
            'будет обработано как число; если выключено — как текст.',
            required=True,
            default=False,
        ),
    ]


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType


class ExecuteView(execute.Execute):
    async def post(self, json: NodeRunContext) -> NodeRunContext:
        try:
            text_field = json.node.data.properties.get('text_field', '')
            number_field = json.node.data.properties.get('number_field', 0)
            field_type = json.node.data.properties.get('field_type', False)
            result = None

            if field_type:
                try:
                    text_field_as_number = int(text_field)
                    result = text_field_as_number + number_field
                except ValueError:
                    raise ValueError(
                        'Невозможно преобразовать текстовое поле в число.'
                    )
            else:
                result = text_field + str(number_field)
            await json.save_result({"result": result})
            json.state = RunState.complete
        except Exception as e:
            self.log.warning(f'Error {e}')
            await json.save_error(str(e))
            json.state = RunState.error
        return json


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView
