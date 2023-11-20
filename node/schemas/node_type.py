from typing import List

from uc_flow_schemas import flow
from uc_flow_schemas.flow import OptionValue, Property



class NodeType(flow.NodeType):
    id: str = 'fe19a64a-c274-412d-a6e8-66b9639e1f3a'
    type: flow.NodeType.Type = flow.NodeType.Type.action
    name: str = 'AlfaCRM'
    displayName: str = 'AlfaCRM'
    icon: str = '<svg><text x="8" y="50" font-size="50">🤖</text></svg>'
    description: str = 'AlfaCRM'
    properties: List[Property] = [
        Property(
            displayName='Действие',
            name='action',
            type=Property.Type.OPTIONS,
            description='Выберите действие',
            options=[
                OptionValue(
                    name='Authorization',
                    value='authorization',
                    description='Авторизация пользователя',
                ),
                OptionValue(
                    name='Customer',
                    value='customer',
                    description='Клиент',
                ),
            ],
        ),
        Property(
            displayName='Hostname',
            name='hostname',
            type=Property.Type.STRING,
            description='Укажите хост',
            required=True,
            displayOptions={"show": {"action": ["authorization"]}},
        ),
        Property(
            displayName='Branch',
            name='branch',
            type=Property.Type.NUMBER,
            description='Укажите ID филиала',
            required=True,
            displayOptions={"show": {"action": ["authorization"]}},
        ),
        Property(
            displayName='Email',
            name='email',
            type=Property.Type.EMAIL,
            description='Введите электронну почту',
            required=True,
            displayOptions={"show": {"action": ["authorization"]}},
        ),
        Property(
            displayName='API key(v2api)',
            name='api_key',
            type=Property.Type.STRING,
            description='Введите ваш API ключ (v2api)',
            required=True,
            displayOptions={"show": {"action": ["authorization"]}},
        ),
        Property(
            displayName='Auth result',
            name='auth_result',
            type=Property.Type.JSON,
            displayOptions={"show": {"action": ["customer"]}},
        ),
        Property(
            displayName='Resource',
            name='resource',
            type=Property.Type.OPTIONS,
            description='Выберите нужную модель',
            displayOptions={"show": {"action": ["customer"]}},
            options=[
                OptionValue(
                    name='Customer',
                    value='customer',
                    description='Пользователь',
                ),
            ],
        ),
        Property(
            displayName='Operation',
            name='operation',
            type=Property.Type.OPTIONS,
            description='Выберите нужную операцию',
            displayOptions={
                "show": {"action": ["customer"], "resource": ["customer"]}
            },
            options=[
                OptionValue(
                    name='Index',
                    value='index',
                    description='Чтение списка с фильтрацией и пейджинацией',
                ),
                OptionValue(
                    name='Create',
                    value='create',
                    description='Создание новой модели',
                ),
                OptionValue(
                    name='Update',
                    value='update',
                    description='Изменение свойств модели',
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            displayOptions={
                "show": {
                    "action": ["customer"],
                    "resource": ["customer"],
                    "operation": ["index"],
                }
            },
            options=[
                Property(
                    displayName='ID',
                    name='id',
                    type=Property.Type.NUMBER,
                    description='Id клиента',
                ),
                Property(
                    displayName='Is Study',
                    name='is_study',
                    type=Property.Type.NUMBER,
                    description='Состояние клиента (0 - лид, 1 - клиент)',
                ),
                Property(
                    displayName='Name',
                    name='name',
                    type=Property.Type.STRING,
                    description='Имя клиента',
                ),
                Property(
                    displayName='Lead Status ID',
                    name='lead_status_id',
                    type=Property.Type.NUMBER,
                    description='Статус id лида',
                ),
                Property(
                    displayName='Page',
                    name='page',
                    type=Property.Type.NUMBER,
                    description='Страница',
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            displayOptions={
                "show": {
                    "action": ["customer"],
                    "resource": ["customer"],
                    "operation": ["create"],
                }
            },
            options=[
                Property(
                    displayName='Is Study',
                    name='is_study',
                    type=Property.Type.NUMBER,
                    description='Состояние клиента (0 - лид, 1 - клиент)',
                ),
                Property(
                    displayName='Name',
                    name='name',
                    type=Property.Type.STRING,
                    description='Имя клиента',
                ),
                Property(
                    displayName='Legal Type',
                    name='legal_type',
                    type=Property.Type.BOOLEAN,
                    description='Тип клиента (1 - физ. лицо, 2 - юр. лицо)',
                    default=False,
                ),
            ],
        ),
        Property(
            displayName='Parameters',
            name='parameters',
            type=Property.Type.COLLECTION,
            displayOptions={
                "show": {
                    "action": ["customer"],
                    "resource": ["customer"],
                    "operation": ["update"],
                }
            },
            options=[
                Property(
                    displayName='ID',
                    name='id',
                    type=Property.Type.NUMBER,
                    description='Id клиента',
                ),
                Property(
                    displayName='Name',
                    name='name',
                    type=Property.Type.STRING,
                    description='Имя клиента',
                ),
            ],
        ),
    ]
