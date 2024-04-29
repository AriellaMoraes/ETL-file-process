from libs.api_extract_lib import consume_api
from libs.files.file_lib import create_folder, create_file


class UserExtract:
    url = "https://dummyjson.com/users"
    folder = "output/extract/users"

    def run(self):
        data = consume_api(self.url)
        for item in data["users"]:
            file_path = f"{self.folder}/user_{item['id']}.json"
            create_folder(self.folder)
            create_file(file_path, item)

