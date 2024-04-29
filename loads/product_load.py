from bases.load_bases import LoadBases
from configs.config import TRANSFORM_DIR
from typing import Dict
from models.products_model import Produto


class ProductLoad(LoadBases):
    transform_data_dir = f'{TRANSFORM_DIR}/product'
    model = Produto

