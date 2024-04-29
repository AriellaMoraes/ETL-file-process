from models.products_model import Produto
from models.users_model import User
from models.carts_model import Cart
from libs.database import engine


def create_tables(models):
    for model in models:
        model.metadata.create_all(engine)
        print(f"Tabela para {model.__name__} criada com sucesso!")


if __name__ == "__main__":
    models_to_create = [Produto, User, Cart]
    create_tables(models_to_create)
