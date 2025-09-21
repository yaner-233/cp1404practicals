choice = ""
while choice != "Q":
    print("Enter name: Guido")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>> ")
    if choice == "H":
        print("Hello Guido")
    elif choice == "G":
        print("Goodbye")
    elif choice == "Q":
        print("Finished.")
    else:
        print("Invalid choice")