"""
CP1404/CP5632 Practical
File and class example - reads a file, stores in objects of custom class, with pointer arithmetic support.
"""

import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    in_file = open('languages.csv', 'r')
    reader = csv.reader(in_file)
    next(reader)

    for row in reader:
        name = row[0]
        typing = row[1]
        reflection = row[2] == "Yes"
        year = int(row[3])
        pointer_arithmetic = row[4] == "Yes"
        language = ProgrammingLanguage(name, typing, reflection, year, pointer_arithmetic)
        languages.append(language)

    in_file.close()

    for language in languages:
        print(language)


def using_csv():
    """" Language file reader version using the csv module."""
    in_file = open('languages.csv', 'r', newline='')
    reader = csv.reader(in_file)
    next(reader)

    for row in reader:
        print(f"Full row: {row}")
        print(f"Language: {row[0]}, Supports Pointer Arithmetic: {row[4] == 'Yes'}\n")

    in_file.close()


def using_namedtuple():
    """Language file reader version using a named tuple."""
    in_file = open('languages.csv', 'r', newline='')
    field_names = in_file.readline().strip().split(',')
    print(f"Field names: {field_names}")
    Language = namedtuple('Language', field_names)
    reader = csv.reader(in_file)


    for row in reader:
        reflection = row[2] == "Yes"
        year = int(row[3])
        pointer_arithmetic = row[4] == "Yes"
        language = Language(row[0], row[1], reflection, year, pointer_arithmetic)
        print(repr(language))
    in_file.close()


def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    field_names = ['name', 'typing', 'reflection', 'year', 'pointer_arithmetic']
    Language = namedtuple('Language', field_names)
    in_file = open("languages.csv", "r", newline='')
    next(in_file)
    reader = csv.reader(in_file)

    for row in reader:
        reflection = row[2] == "Yes"
        year = int(row[3])
        pointer_arithmetic = row[4] == "Yes"
        language = Language(row[0], row[1], reflection, year, pointer_arithmetic)
        support_status = "supports" if language.pointer_arithmetic else "does not support"
        print(f"{language.name} ({language.year}) {support_status} pointer arithmetic")
        print(repr(language))

    in_file.close()


if __name__ == "__main__":
    main()
