from Transforms.product_transform import ProductTransform
from Transforms.cart_transform import CartTransform
from Transforms.user_transform import UserTransform

transformes_mapping = {
    "products": ProductTransform,
    "carts": CartTransform,
    "users": UserTransform
}


def transform_from_api(transformes):

    for transform in transformes:
        if transform in transformes_mapping:
            extractor_class = transformes_mapping[transform]
            extractor_instance = extractor_class()
            extractor_instance.run()


if __name__ == "__main__":
    transform_from_api(["products", "carts", "users"])

