"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"



    car = Car()
    assert car.odometer == 0, "Car does not set odometer correctly"

    car_default_fuel = Car()
    assert car_default_fuel.fuel == 0, "The default fuel quantity setting of the Car is incorrect."
    car_custom_fuel = Car(fuel=10)
    assert car_custom_fuel.fuel == 10, "Incorrect custom fuel level setting for Car"




run_tests()


doctest.testmod()


def format_sentence(phrase):
    """
    Format the phrase into a sentence: capitalize the first letter and end with a period.
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("coding is fun")
    'Coding is fun.'
    """
    if not phrase:
        return ""
    sentence = phrase[0].upper() + phrase[1:]
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence
