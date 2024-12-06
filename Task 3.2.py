#Day3
#Question 2 :
#Create a menu driven program and store and retrive data using Dictionaries
data = {'name':'adithyan','age':18,'clg':'sct'}
repeat=1
while repeat==1:
    print("Menu:")
    print("1. Add data")
    print("2. Retrieve data")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        key = input("Enter key: ")
        value = input("Enter value: ")
        data[key] = value
        print("Data added.")
    elif choice == 2:
        key = input("Enter key to retrieve: ")
        if key in data:
            print("Value:", data[key])
        else:
            print("Key not found.")
    elif choice == 3:
        print("Exiting program.")
        repeat=0
    else:
        print("Invalid choice.")
