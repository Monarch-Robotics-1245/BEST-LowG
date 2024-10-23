import pytest

def test_is_true():
    assert True

def test_equals():
    for i in [-3, -2, -1, 0, 1, 2, 3]:
        assert equal(i)

def test_not_equals():
    for i in [-3, -2, -1, 0, 1, 2, 3]:
        assert not_equal(i, i+1)

def not_equal(a, b):
    return a != b

def equal(a):
    return a == a

def test_is_not_true():
    assert not False

def test_greater_than():
    tuples_list = [(x, y) for x in range(10) for y in range(10) if x > y]
    for i in range(len(tuples_list)):
        assert greater_than(tuples_list[i][0], tuples_list[i][1])

def greater_than(a, b):
    return a > b

def test_greater_than_or_equal_to():
    tuples_list = [(x, y) for x in range(10) for y in range(10) if x >= y]
    for i in range(len(tuples_list)):
        assert greater_than_or_equal_to(tuples_list[i][0], tuples_list[i][1])

def greater_than_or_equal_to(a, b):
    return a >= b

def test_not_one():
    assert not 1 == 0

def test_less_than():
    tuples_list = [(x, y) for x in range(10) for y in range(10) if x < y]
    for i in range(len(tuples_list)):
        assert less_than(tuples_list[i][0], tuples_list[i][1])

def less_than(a, b):
    return a < b

def test_positive_check():
    for i in [1, 2, 3, 4, 5]:
        assert is_positive(i)

def is_positive(a):
    return a > 0

def test_is_even():
    for i in [0, 2, 4, 6, 8]:
        assert is_even(i)

def is_even(a):
    return a % 2 == 0

def test_is_odd():
    for i in [1, 3, 5, 7, 9]:
        assert is_odd(i)

def is_odd(a):
    return a % 2 != 0

def test_is_not_negative():
    for i in [0, 1, 2, 3, 4]:
        assert not_negative(i)

def not_negative(a):
    return a >= 0

def test_is_zero():
    assert is_zero(0)

def is_zero(a):
    return a == 0

def test_absolute_value():
    for i in [-1, -2, -3]:
        assert abs(i) == -i

def test_is_non_zero():
    for i in [1, -1, 2, -2, 3]:
        assert is_non_zero(i)

def is_non_zero(a):
    return a != 0

def test_sum():
    assert sum_two(2, 3) == 5

def sum_two(a, b):
    return a + b

def test_difference():
    assert difference(5, 3) == 2

def difference(a, b):
    return a - b

def test_division():
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5

def divide(a, b):
    return a / b if b != 0 else None

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(5) == 120

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def test_string_equality():
    assert string_equal("hello", "hello")
    assert not string_equal("hello", "world")

def string_equal(a, b):
    return a == b
