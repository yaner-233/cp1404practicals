def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9.0

def main():
    print("MENU: C (C→F) | F (F→C) | Q (Quit)")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            c = float(input("Celsius: "))
            print(f"Result: {celsius_to_fahrenheit(c):.2f} F")
        elif choice == "F":
            f = float(input("Fahrenheit: "))
            print(f"Result: {fahrenheit_to_celsius(f):.2f} C")
        else:
            print("Invalid choice!")
        choice = input(">>> ").upper()

if __name__ == "__main__":
    main()