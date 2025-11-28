import csv
from guitar import Guitar


def load_guitars(filename):
    """Load guitars from a CSV file and return a list."""
    guitars = []
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                name = row[0]
                year = int(row[1])
                cost = float(row[2])
                guitars.append(Guitar(name, year, cost))
        print(f"Loaded {len(guitars)} guitars from {filename}")
    except FileNotFoundError:
        print(f"Note: {filename} not found. Starting with empty list.")
    return guitars


def save_guitars(guitars, filename):
    """Save all guitars in the list to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Year", "Cost"])
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])
    print(f"Saved {len(guitars)} guitars to {filename}")


def display_guitars(guitars, title):
    """Display a formatted list of guitars with a given title."""
    print(f"\n{title}")
    if not guitars:
        print("No guitars to display.")
        return
    for i, guitar in enumerate(guitars, 1):
        print(f"{i}. {guitar}")


def get_user_guitars():
    """Prompt user to enter new guitars and return a list of Guitar objects."""
    new_guitars = []
    print("Enter new guitars (leave name empty to stop)")
    continue_entering = True
    while continue_entering:
        name = input("Guitar name: ").strip()
        if not name:
            continue_entering = False
        else:
            valid_year = False
            while not valid_year:
                year_input = input("Year made: ").strip()
                try:
                    year = int(year_input)
                    valid_year = True
                except ValueError:
                    print("Invalid year. Please enter an integer.")

            valid_cost = False
            while not valid_cost:
                cost_input = input("Cost: $").strip()
                try:
                    cost = float(cost_input)
                    valid_cost = True
                except ValueError:
                    print("Invalid cost. Please enter a number.")

            new_guitar = Guitar(name, year, cost)
            new_guitars.append(new_guitar)
            print(f"Added: {new_guitar}")

    return new_guitars


def main():
    """Main function to coordinate loading, displaying, adding, sorting, and saving guitars."""
    filename = "guitars.csv"

    guitars = load_guitars(filename)

    display_guitars(guitars, "Current Guitars")

    new_guitars = get_user_guitars()
    if new_guitars:
        guitars.extend(new_guitars)
        print(f"Added {len(new_guitars)} new guitar(s) to the list.")

    guitars.sort()
    display_guitars(guitars, "Guitars Sorted by Year (Oldest to Newest)")

    save_guitars(guitars, filename)


if __name__ == "__main__":
    main()