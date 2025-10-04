numbers = []
for i in range(5):
    number_input = input(f"Enter a number: ")
    number = float(number_input)
    numbers.append(number)

for sum_number in numbers:
    print("Number: ",sum_number)

print("The first number is: ",numbers[0])
print("The last number is: ",numbers[-1])
print("The smallest number is: ",min(numbers))
print("The largest number is: ",max(numbers))
print("The average number is: ",sum(numbers)/len(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name = input("Enter your name: ")
if name in usernames:
    print("Access granted")
else:
    print("Access denied")