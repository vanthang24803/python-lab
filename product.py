# product.py

from convert import convertMoney

class Product:
    def __init__(
        self, name: str, price: float, description: str, image: str, star: int
    ) -> None:
        self.name = name
        self.price = price
        self.description = description
        self.image = image
        self.star = star

    def display(self):
        print(
            f"Name: {self.name}, Price: {convertMoney(self.price)} VND, Description: {self.description}, Star: {self.star}"
        )
