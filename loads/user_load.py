from bases.load_bases import LoadBases
from configs.config import TRANSFORM_DIR
from models.users_model import User


class UserLoad(LoadBases):
    transform_data_dir = f'{TRANSFORM_DIR}/user'
    model = User
