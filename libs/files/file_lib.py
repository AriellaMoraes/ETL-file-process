import os
import json
from typing import List, Dict


def create_folder(folder: str):
    os.makedirs(folder, exist_ok=True)


def create_file(folder: str, data: List | Dict):
    with open(folder, "w") as file:
        json.dump(data, file)
        print(f"Arquivo {folder} criado com sucesso!")


def read_file(folder: str) -> List | Dict:
    with open(folder, 'r') as file:
        data = json.load(file)
        return data



