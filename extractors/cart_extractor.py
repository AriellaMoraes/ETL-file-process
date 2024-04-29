from libs.api_extract_lib import consume_api
from libs.files.file_lib import create_folder, create_file


class CartExtract:
    url = "https://dummyjson.com/carts"
    folder = "output/extract/carts"

    def run(self):
        data = consume_api(self.url)
        for item in data["carts"]:
            file_path = f"{self.folder}/cart_{item['id']}.json"
            create_folder(self.folder)
            create_file(file_path, item)

