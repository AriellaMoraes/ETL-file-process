from configs.config import EXTRACT_DIR
from bases.transform_bases import TransformBase
import os
from configs.config import BASE_DIR
from typing import List, Dict, Any


class ProductTransform(TransformBase):
    extract_data_dir = f'{EXTRACT_DIR}/products'
    mapping_fields = {
        "id":"id_api",
        "title": "titulo",
        "description": "descricao",
        "price": "preco",
        "discountPercentage": "desconto",
        "rating": "nota",
        "stock": "estoque",
        "brand": "marca",
        "category": "categoria"
    }

    name_file = "product"
    transform_data_dir = os.path.join(BASE_DIR, "output", "transform", "product")

