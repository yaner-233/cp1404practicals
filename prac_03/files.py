# files.py

name = input("Enter your name: ")
with open("name.txt", "w") as name_file:
    name_file.write(name)
print("Name saved to 'name.txt' successfully.\n")


with open("name.txt", "r") as name_file:
    saved_name = name_file.read().strip()
print(f"Hi {saved_name}!")
print()


with open("numbers.txt", "w") as num_file:
    num_file.write("40\n19\n3")
with open("numbers.txt", "r") as num_file:
    first_num = int(num_file.readline().strip())
    second_num = int(num_file.readline().strip())
sum_first_two = first_num + second_num
print(f"Sum of first two numbers: {sum_first_two}")
print()


total = 0
with open("numbers.txt", "r") as num_file:
    for line in num_file:
        total += int(line.strip())
print(f"Total of all numbers: {total}")