def main():
    n=int(input("Enter a number n: "))
    total=sum_squares(n)
    print("The sum of squares of first ",n,"natural numbers is: ",total)
def sum_squares(n):
    total=0
    for i in range(1,n+1):
        total= total + i**2  
    return total      
main()        