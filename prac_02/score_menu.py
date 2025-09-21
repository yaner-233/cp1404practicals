from score import determine_result

def get_score():
    while True:
            s = int(input("Score (0-100): "))
            if 0 <= s <= 100:
                return s
            print("Invalid score!")

def show_stars(score):
    print("*" * score)

def main():
    current_score = None
    print("Menu:\n(G)et score\n(P)rint result\n(S)how stars\n(Q)uit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            current_score = get_score()
        elif choice == "P":
            if current_score is not None:
                print(f"Result: {determine_result(current_score)}")
            else:
                print("Get a score first!")
        elif choice == "S":
            if current_score is not None:
                show_stars(current_score)
            else:
                print("Get a score first!")
        else:
            print("Invalid choice!")
        choice = input(">>> ").upper()
    print("Farewell!")

if __name__ == "__main__":
    main()