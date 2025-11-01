from guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    is_input = True
    while is_input:
        name = input("Name: ")
        if not name:
            is_input = False
        else:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
            print(f"{guitar} added.")

# guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))
# guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == "__main__":
    main()