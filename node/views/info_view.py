from uc_flow_nodes.views import info

from node.schemas.node_type import NodeType


class InfoView(info.Info):
    class Response(info.Info.Response):
        node_type: NodeType
