from configs.config import EXTRACT_DIR
from bases.transform_bases import TransformBase
import os
from configs.config import BASE_DIR
from typing import List, Dict, Any


class CartTransform(TransformBase):
    extract_data_dir = f'{EXTRACT_DIR}/carts'
    mapping_fields = {
        "id": "id_api",
        "products": "produtos"
    }

    name_file = "cart"
    transform_data_dir = os.path.join(BASE_DIR, "output", "transform", "cart")

    def _make_mapping(self, item: Dict[str, Any]) -> Dict[str, Any]:
        novo_item = super()._make_mapping(item)
        # Mapeia apenas os IDs dos produtos
        novo_item['produtos'] = [produto['id'] for produto in novo_item['produtos']]
        return novo_item
