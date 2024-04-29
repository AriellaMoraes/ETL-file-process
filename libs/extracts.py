from extractors.product_extractor import ProductExtract
from extractors.cart_extractor import CartExtract
from extractors.user_extractor import UserExtract

extractors_mapping = {
    "products": ProductExtract,
    "carts": CartExtract,
    "users": UserExtract
}


def extract_from_api(extractors):

    for extract in extractors:
        if extract in extractors_mapping:
            extractor_class = extractors_mapping[extract]
            extractor_instance = extractor_class()
            extractor_instance.run()






