from shopping_cart import to_usd, find_tax, find_total


def test_to_usd():
    """
    Tests the to_usd function.
    """
    assert to_usd(1000.2342) == "$1,000.23"
    assert to_usd(100.23) == "$100.23"
    assert to_usd(100.2) == "$100.20"

def test_find_tax():
    """
    Tests the find_tax function.
    """
    assert ("{0:,.6f}".format(find_tax(10.882))) == "0.952175"
    assert find_tax(0) == 0

def test_find_total():
    """
    Tests the find_total function.
    """
    return find_total(10.882, 0.952175) == 11.834175
    assert find_total(10.882, 0) == 10.882