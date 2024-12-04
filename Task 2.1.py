n=int(input("Enter a number: "))
p=1
if n==2 or n==3:
    print(n,"is a Prime Numbers")
elif n!=2 and n!=3:
    for i in range(2,n):
        if n%i==0:
            p=0
            print(n,"is not a Prime Numbers")
            break
if p==1:
    print(n,"is a Prime Numbers")
