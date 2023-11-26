import requests

from product import Product
from convert import convertMoney
from api import BASRE_URL

if __name__ == "__main__":

    URL = f"{BASRE_URL}/products"

    totalPrice = 0

    response = requests.get(url=URL)

    if response.status_code == 200:
        data = response.json()
        products = data["products"]

        for product_data in products:
            product = Product(
                product_data["name"],
                product_data["price"],
                product_data["description"],
                product_data["image"],
                product_data["star"],
            )
            product.display()

            totalPrice += product_data["price"]

        print(
            f"\nTotal price of products is {convertMoney(totalPrice)} and Sum of Products is {data['totalProducts']}\n"
        )
    else:
        print(f"Error {response.status_code}")
