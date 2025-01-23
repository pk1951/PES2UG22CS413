import json
from products import Product, get_product
from cart import dao


class Cart:
    """
    Represents a shopping cart for a user.
    """
    def __init__(self, id: int, username: str, contents: list[Product], cost: float):
        self.id = id
        self.username = username
        self.contents = contents
        self.cost = cost

    @staticmethod
    def load(data: dict):
        """
        Loads a Cart instance from a dictionary.
        """
        return Cart(
            id=data['id'],
            username=data['username'],
            contents=data['contents'],
            cost=data['cost']
        )


def get_cart(username: str) -> list[Product]:
    """
    Retrieves the cart for a given username, loading product details.
    """
    cart_details = dao.get_cart(username)
    if not cart_details:
        return []

    # Use list comprehension for concise processing
    items = [
        product_id
        for cart_detail in cart_details
        for product_id in eval(cart_detail['contents'])  # Avoid eval if possible
    ]

    # Retrieve product details efficiently
    return [get_product(product_id) for product_id in items]


def add_to_cart(username: str, product_id: int):
    """
    Adds a product to the user's cart.
    """
    dao.add_to_cart(username, product_id)


def remove_from_cart(username: str, product_id: int):
    """
    Removes a product from the user's cart.
    """
    dao.remove_from_cart(username, product_id)


def delete_cart(username: str):
    """
    Deletes the cart for the specified username.
    """
    dao.delete_cart(username)
