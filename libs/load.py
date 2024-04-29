from loads.product_load import ProductLoad
from loads.user_load import UserLoad
from loads.cart_load import CartLoad


class LoadFactory:
    @staticmethod
    def run_loads():
        ProductLoad().run()
        UserLoad().run()
        CartLoad().run()


if __name__ == "__main__":
    LoadFactory.run_loads()