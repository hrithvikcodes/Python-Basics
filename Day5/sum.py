def main():
    n=int(input("Enter a number n:"))
    total= sum_natural(n)
    print("The sum of first",n,"natural numbers is: ",total)
def sum_natural(n):
    total=0
    for i in range(1,n+1):
        total=total+i #accumulate the sum
    return total
    
main()