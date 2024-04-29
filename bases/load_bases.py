from libs.files.file_lib import read_file
import os
from typing import List, Dict, Any
from libs.database import Session


class LoadBases:
    transform_data_dir = None
    model = None

    def __init__(self):
        self.data_load: List[Dict[str, Any]] = []

    def read_transform(self):
        for filename in os.listdir(self.transform_data_dir):
            filepath = os.path.join(self.transform_data_dir, filename)
            data = read_file(filepath)
            self.data_load.append(data)

    def save_to_database(self):
        with Session() as session:
            for data in self.data_load:
                novo_produto = self.model(**data)
                session.add(novo_produto)
            session.commit()
            print("Tabela criada com sucesso")

    def run(self):
        self.read_transform()
        self.save_to_database()

