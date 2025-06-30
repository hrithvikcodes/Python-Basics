def main():
    x=int(input("Enter a number x: "))
    if is_even(x):
        print("X is Even!")
    else:
        print("X is Odd!")
def is_even(x):
    if x%2==0 :
        return True
    else: 
        return False
main()    