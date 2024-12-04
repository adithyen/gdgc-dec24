#Day 2
#Question 2 :
#Create a program two print all values of a 12 hour clock ( with AM and PM ) , one by one with 1 second delay
import time
l = ["AM", "PM"]
for i in l:
    for h in range(1, 13): 
        for m in range(60):
            for s in range(60):
                if h<10:
                    hr = '0'+str(h)
                else:
                    hr=str(h)
                if m<10:
                    mn = '0'+str(m)
                else:
                    mn=str(m)
                if s<10:
                    sc = '0'+str(s)
                else:
                    sc=str(s)
                t= hr + ":" + mn + ":" + sc + " " + i
                print(t)
                time.sleep(1) 
