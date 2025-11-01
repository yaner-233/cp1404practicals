"""
Word Occurrences
Estimate: 45 minutes
Actual:   50 minutes
"""
from guitar import Guitar


def test_guitar_methods():
    gibson = Guitar("Gibson L-5 CES", 1922)
    gibson_age = 100
    actual_age_gibson = 2025-gibson.year
    print(f"Gibson L-5 CES get_age() - Expected {gibson_age}. Got {actual_age_gibson}")

    expected_vintage_gibson = True
    actual_vintage_gibson = 2025-gibson.year
    if expected_vintage_gibson >= 50:
        actual_vintage_gibson = True
    else:
        actual_vintage_gibson = False
    print(f"Gibson L-5 CES is_vintage() - Expected {expected_vintage_gibson}. Got {actual_vintage_gibson}")

    another_guitar = Guitar("Another Guitar", 2013)
    expected_age_another = 9
    actual_age_another = 2025-another_guitar.year
    print(f"Another Guitar get_age() - Expected {expected_age_another}. Got {actual_age_another}")

    expected_vintage_another = False
    actual_vintage_another = 2025-another_guitar.year
    if expected_vintage_another >= 50:
        actual_vintage_another = True
    else:
        actual_vintage_another = False
    print(f"Another Guitar is_vintage() - Expected {expected_vintage_another}. Got {actual_vintage_another}")


if __name__ == "__main__":
    test_guitar_methods()