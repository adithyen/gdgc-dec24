money = float(input("How much money do you have? "))
percent= float(input("What percentage of your money would you like to spend? "))
limit = (percent/ 100) * money
item1 = float(input("Enter the cost of the first item: "))
item2 = float(input("Enter the cost of the second item: "))
item3 = float(input("Enter the cost of the third item: "))
spend = item1 + item2 + item3
if spend <= limit:
    print("You can buy more")
else:
    print("You can't buy more")
