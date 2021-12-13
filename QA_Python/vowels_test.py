import vowels


def test_with_vowels():
    assert vowels.vowels("Cat") == 1
    assert vowels.vowels("House") == 3
    assert vowels.vowels("aeiou") == 5
    assert vowels.vowels("AEIOU") == 5


def test_without_vowels():
    assert vowels.vowels("qwrtyp") == 0
    assert vowels.vowels("SDFGHJKL") == 0
