from libs.api_extract_lib import consume_api
from libs.files.file_lib import create_folder, create_file


class ProductExtract:
    url = "https://dummyjson.com/products?limit=100"
    extract_data_dir = "output/extract/products"

    def run(self):
        data = consume_api(self.url)
        for item in data["products"]:
            file_path = f"{self.extract_data_dir}/product_{item['id']}.json"
            create_folder(self.extract_data_dir)
            create_file(file_path, item)





