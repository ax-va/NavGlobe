from core.schema.base_node_layer import BaseNodeLayer


class _NodeLayerSP(BaseNodeLayer):
    @property
    def NODE_INDEX_OFFSET_FOR_LAYER(self) -> int:
        if self._node_index_offset_for_layer is None:
            self._node_index_offset_for_layer: int = self._schema.constants.south_pole.node.INDEX
        return self._node_index_offset_for_layer

    @property
    def NUMBER_OF_NODES(self) -> int:
        if self._number_of_nodes is None:
            self._number_of_nodes = 1
        return self._number_of_nodes