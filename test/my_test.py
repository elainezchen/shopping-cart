from shopping_cart import to_usd


def test_to_usd():
    """
    Tests the to_usd function.
    """
    assert to_usd(1000.2342) == "$1,000.23"