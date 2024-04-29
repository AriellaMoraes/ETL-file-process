from configs.config import EXTRACT_DIR
from bases.transform_bases import TransformBase
import os
from configs.config import BASE_DIR


class UserTransform(TransformBase):
    extract_data_dir = f'{EXTRACT_DIR}/users'
    mapping_fields = {
        "id": "id_api",
        "firstName": "nome",
        "lastName": "sobrenome",
        "maidenName": "nomeprincipal",
        "age": "idade",
        "gender": "genero",
        "phone": "telefone",
        "username": "username",
        "password": "password",
        "birthDate": "aniversario"
    }

    name_file = "user"
    transform_data_dir = os.path.join(BASE_DIR, "output", "transform", "user")