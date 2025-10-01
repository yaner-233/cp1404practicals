# files.py
from fileinput import close
#1
name = input("Enter your name: ")
name_file = open("name.txt", "w")
name_file.write(name)
name_file.close()
print("Name saved to 'name.txt' successfully.\n")


#2
name_file = open("name.txt", "r")
saved_name = name_file.read().strip()
name_file.close()
print(f"Hi {saved_name}!")
print()

#3
with open("numbers.txt", "w") as num_file:
    num_file.write("40\n19\n3")
with open("numbers.txt", "r") as num_file:
    first_num = int(num_file.readline().strip())
    second_num = int(num_file.readline().strip())
num_first_two = first_num + second_num
print(f"{num_first_two}")
print()

#4
total = 0
with open("numbers.txt", "r") as num_file:
    for line in num_file:
        total += int(line.strip())
print(f"Total of all numbers: {total}")