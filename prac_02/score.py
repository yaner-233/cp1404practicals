def get_valid_score():
    while True:
            score = int(input("Enter score (0-100): "))
            if 0 <= score <= 100:
                return score
            print("Score must be 0-100!")

def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = get_valid_score()
    print(f"Result: {determine_result(score)}")

if __name__ == "__main__":
    main()