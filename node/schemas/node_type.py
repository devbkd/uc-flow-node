from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import OptionValue, Property

from node.schemas.enums import SwitchValues


class NodeType(flow.NodeType):
    id: str = 'fe19a64a-c274-412d-a6e8-66b9639e1f3a'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'GoogleExtension'
    displayName: str = 'GoogleExtension'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    description: str = 'GoogleExtension'
    properties: List[Property] = [
        Property(
            displayName='Переключатель',
            name='switch_field',
            type=Property.Type.BOOLEAN,
            placeholder='Включено/Выключено',
            required=True,
            default=False,
        ),
        Property(
            displayName='Значение 1',
            name='value_1',
            type=Property.Type.OPTIONS,
            required=False,
            default='',
            options=[
                OptionValue(
                    name='Значение 1',
                    value=SwitchValues.value1,
                    description='',
                ),
                OptionValue(
                    name='Значение 2',
                    value=SwitchValues.value2,
                    description='',
                ),
            ],
            displayOptions={
                "show": {"switch_field": [True]},
                "hide": {"switch_field": [False]},
            },
        ),
        Property(
            displayName='Значение 2',
            name='value_2',
            type=Property.Type.OPTIONS,
            required=False,
            default='',
            options=[
                OptionValue(
                    name='Значение 1',
                    value=SwitchValues.value1,
                    description='',
                ),
                OptionValue(
                    name='Значение 2',
                    value=SwitchValues.value2,
                    description='',
                ),
            ],
            displayOptions={
                "show": {"switch_field": [True]},
                "hide": {"switch_field": [False]},
            },
        ),
        Property(
            displayName='Поле для ввода почты',
            name='email_input',
            type=Property.Type.STRING,
            required=False,
            default='',
            displayOptions={
                "show": {
                    "value_1": [SwitchValues.value1],
                    "value_2": [SwitchValues.value1],
                },
                "hide": {
                    "value_1": [SwitchValues.value2],
                    "value_2": [SwitchValues.value2],
                },
            },
        ),
        Property(
            displayName='Поле для ввода даты и времени',
            name='datetime_input',
            type=Property.Type.DATETIME,
            required=False,
            default='',
            displayOptions={
                "show": {
                    "value_1": [SwitchValues.value2],
                    "value_2": [SwitchValues.value2],
                },
                "hide": {
                    "value_1": [SwitchValues.value1],
                    "value_2": [SwitchValues.value1],
                },
            },
        ),
    ]
