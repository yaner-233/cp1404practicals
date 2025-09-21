#for i in range(1, 21, 2):
    #print(i, end=' ')
#print()

#for i in range(0, 101, 10):
   # print(i, end=" ")

#for i in range(20, 0, -1):
    #print(i, end=' ')

#number = int(input("Enter a number: "))
#print("Number of stars :", number)
#print("*" * number)


number = int(input("Enter a number: "))
for i in range(number):
    number = "*" * (i+1)
    print(number)

