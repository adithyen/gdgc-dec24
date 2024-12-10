#Day 2
#Question 3 :/Bonus Question :
#Create a menu driven program to  add name , remove name , check if name is present , display all names from a list
names = []
while True:
    print("1.add name")
    print("2.check name")
    print("3.remove name")
    print("4.show names")
    print("5.exit")
    command = input("command: ")
    if command == "1":
        name = input("enter name: ")
        names.append(name)
    if command == "2":
        name = input("enter name: ")
        if name in names:
            print("name is present")
        else:
            print("name is not present")
    if command == "3":
        name = input("enter name: ")
        if name in names:
            names.remove(name)
        else:
            print("name not found")
    if command == "4":
        print("the names are:")
        for name in names:
            print(name)
    if command == "5":
        print("Program exited")
        break
    if command not in ["1", "2", "3", "4", "5"]:
        print("invalid command")
