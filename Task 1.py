#Day 1
#Question 1 :
'''- asks user how much money do you have with them
- asks how much percent of it they would like to spend
- then take cost of items they have bought seprately ( assume they only take 3 items)
- if the total cost is less than the amout they can spend , tell them the can buy it
- else , tell the they can buy it'''
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
