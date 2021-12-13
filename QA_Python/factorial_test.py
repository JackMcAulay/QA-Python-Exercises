import factorial


def test_factorial():
    assert factorial.factorial(1) == 1
    assert factorial.factorial(5) == 120
    assert factorial.factorial(8) == 40320


