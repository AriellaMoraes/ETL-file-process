import os

from libs.files.file_lib import read_file, create_file, create_folder
from typing import List, Dict, Any


class TransformBase:
    extract_data_dir = None
    mapping_fields: Dict[str, str]
    transform_data_dir = None
    name_file = None

    def __init__(self):
        self.data_items: List[Dict[str, Any]] = []
        self.data_transform: List[Dict[str, Any]] = []

    def _data_item_generate(self):
        for filename in os.listdir(self.extract_data_dir):
            filepath = os.path.join(self.extract_data_dir, filename)
            data = read_file(filepath)
            self.data_items.append(data)

    def _make_mapping(self, item: Dict[str, Any]) -> Dict[str, Any]:
        novo_item = {}
        for k, v in self.mapping_fields.items():
            novo_item[v] = item[k]
        return novo_item

    def _transform_data(self):
        for item in self.data_items:
            novo_item = self._make_mapping(item)
            self.data_transform.append(novo_item)
        print(self.data_transform)

    def _create_data(self):
        for dado in self.data_transform:
            file_path = os.path.join(self.transform_data_dir, f"{self.name_file}_{dado['id_api']}.json")
            create_folder(self.transform_data_dir)
            create_file(file_path, dado)

    def run(self):
        self._data_item_generate()
        self._transform_data()
        self._create_data()
