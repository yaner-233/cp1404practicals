def get_password():
    return input("Enter password: ")

def print_stars(password):
    print("*" * len(password))

def main():
    pwd = get_password()
    print_stars(pwd)

if __name__ == "__main__":
    main()