def main():
    x=int(input("Enter a number x : "))
    y=int(input("Enter a number y : "))
    n=GCD(x,y)
    print("The greatest common divisor of ",x,"and",y,"is : ",n)
def GCD(x,y):
    GCD_VAL=0
    for i in range(1,min(x,y)+1):
        if x%i==0 and y%i==0 :
            GCD_VAL = i
        return GCD_VAL
main()        

     
