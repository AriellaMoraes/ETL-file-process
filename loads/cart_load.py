from bases.load_bases import LoadBases
from configs.config import TRANSFORM_DIR
from models.carts_model import Cart


class CartLoad(LoadBases):
    transform_data_dir = f'{TRANSFORM_DIR}/cart'
    model = Cart
