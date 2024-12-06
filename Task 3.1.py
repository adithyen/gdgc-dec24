#Day3
#Question 1 :
#Program to multiply two matrix which is in the form of a 2d list
m1 = [[1, 2], [3, 4]]
m2 = [[5, 6], [7, 8]]
r1 = len(m1)
c1 = len(m1[0])
r2 = len(m2)
c2 = len(m2[0])
p = [] 
for _ in range(r1): 
    row = []  
    for _ in range(c2):  
        row.append(0)  
    p.append(row)
for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            p[i][j] += m1[i][k] * m2[k][j]
print(p)
