from tokenize import group

while True:
    number = int(input("Enter a number: "))
    if number >= 0:
        break
    else:
        print("Invalid number of items!")

total = 0
prices = []
for i in range (number):
    price = float(input("Enter price: "))
    prices.append(price)
    total = total + price
print("Number of items: ", number)
for price in prices:
    print("Price of item: ", price)
if total > 100:
    total = total * 0.9
print(f"Total price for {number} items is ${total:.2f}")