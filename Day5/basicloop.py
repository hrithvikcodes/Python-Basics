for i in range(1,11): #print numbers from 1 to 10
    print(i)

print("Even numbers between 10 and 30: ")
for i in range(11,30):
    if i%2==0:
        print(i)

print("numbers in reverse from 10 to 1:")
for i in range(10,0,-1): #range(start=10,stop=0,step=-1)
    print(i)

print("numbers in reverse order from 20 to 10:")
i = 20
while i >= 10:
    print(i)
    i = i-1
