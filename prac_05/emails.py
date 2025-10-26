"""
Word Occurrences
Estimate: 20 minutes
Actual:   35 minutes
"""


def name_from_email(email):
    name_part = email.split("@")[0]
    return name_part.title()


def main():
    email_to_name = {}
    continue_input = True
    while continue_input:
        email = input("Email: ")
        if not email:
            continue_input = False
        else:
            suggested_name = name_from_email(email)
            response = input(f"Is your name {suggested_name}? (Y/n) ")

            if response in ["n", "no"]:
                name = input("Name: ").strip()
            else:
                name = suggested_name

        email_to_name[email] = name


    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()


