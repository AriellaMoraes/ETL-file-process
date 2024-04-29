import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # diretorio /api
EXTRACT_DIR = f'{BASE_DIR}/output/extract'
TRANSFORM_DIR = f'{BASE_DIR}/output/transform'
HOST = "localhost"
PORT = 5432
DBNAME = "postgres"
USER = "postgres"
PASSWORD = "postgres"


