from api.Helpers import minDigit, minSize, minLowercase, \
    minSpecialChars, minUppercase, noRepeted
from api.queries import verify_resolver


def test_password_less_than_indicated():
    result = minSize("123", 4)
    assert False == result

def test_password_equal_than_indicated():
    result = minSize("1234", 4)
    assert True == result

def test_password_greater_than_indicated():
    result = minSize("123456", 4)
    assert True == result

def test_uppercases_less_than_indicated():
    result = minUppercase("aA", 4)
    assert False == result

def test_uppercases_equal_than_indicated():
    result = minUppercase("12AAA34", 3)
    assert True == result

def test_uppercases_greater_than_indicated():
    result = minUppercase("123AAAAA456", 2)
    assert True == result

def test_lowercases_less_than_indicated():
    result = minLowercase("aA", 4)
    assert False == result

def test_lowercases_equal_than_indicated():
    result = minLowercase("12aaa34", 3)
    assert True == result

def test_lowercases_greater_than_indicated():
    result = minLowercase("123Aaaaa456", 2)
    assert True == result

def test_digits_less_than_indicated():
    result = minDigit("aA", 4)
    assert False == result

def test_digits_equal_than_indicated():
    result = minDigit("2aaa34", 3)
    assert True == result

def test_digits_greater_than_indicated():
    result = minDigit("123Aaaaa456", 2)
    assert True == result

def test_special_chars_less_than_indicated():
    result = minSpecialChars("!aA", 4)
    assert False == result

def test_special_chars_equal_than_indicated():
    result = minSpecialChars("!@#a34", 3)
    assert True == result

def test_special_chars_greater_than_indicated():
    result = minSpecialChars("123@%&Aaaaa456", 2)
    assert True == result

def test_password_sequence_repeated_chars():
    result = noRepeted("!aa", 0)
    assert False == result

def test_password_no_sequence_repeated_chars():
    result = noRepeted("!aBa", 0)
    assert True == result
