def main():
    n=int(input("Enter a number n: "))
    total=sum_of_cubes(n)
    print("The sum of cubes of first ",n,"natural numbers is :",total)
def sum_of_cubes(n):
    total=0
    for i in range(1,n+1):
        total= total + i**3
    return total    
main()