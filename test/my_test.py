from shopping_cart import to_usd
from shopping_cart import find_product


def test_to_usd():
    """
    Tests the to_usd function.
    """
    assert to_usd(1000.2342) == "$1,000.23"
    assert to_usd(100.23) == "$100.23"
    assert to_usd(100.2) == "$100.20"

def test_find_product():
    """
    Tests the find_product function.
    """
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    ]

    x = "0"
    matching_products = find_product(products)
    assert "Chocolate Sandwich Cookies" in matching_products[0]["name"]