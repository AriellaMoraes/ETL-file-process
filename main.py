from libs.extracts import extract_from_api


if __name__ == "__main__":
    extract_from = extract_from_api(["products", "carts", "users"])

