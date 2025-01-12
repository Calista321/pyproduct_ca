from pyproduct_ca import product_numbers

def test_product_numbers():
    """
    Test cases for the product_numbers function.
    """

    # Test with positive integers
    assert product_numbers(2, 3) == 6, "Failed on positive integers"

    # Test with a positive and a negative integer
    assert product_numbers(-4, 5) == -20, "Failed on a positive and a negative integer"

    # Test with two negative integers
    assert product_numbers(-7, -3) == 21, "Failed on two negative integers"

    # Test with zero
    assert product_numbers(0, 5) == 0, "Failed when the first number is zero"
    assert product_numbers(5, 0) == 0, "Failed when the second number is zero"

    # Test with floating-point numbers
    assert product_numbers(2.5, 4) == 10.0, "Failed on a float and an integer"
    assert product_numbers(1.5, 1.5) == 2.25, "Failed on two floats"

    # Test with large numbers
    assert product_numbers(1e10, 2) == 2e10, "Failed on large numbers"

    print("All tests passed.")

test_product_numbers()