from typing import List

import ujson
from uc_flow_nodes.schemas import NodeRunContext
from uc_flow_nodes.service import NodeService

from node.views.execute_view import ExecuteView
from node.views.info_view import InfoView


class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView
