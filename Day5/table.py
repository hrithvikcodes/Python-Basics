def main():
    x=int(input("Enter a number x: "))
    table(x)
def table(x):
    for i in range (1,11):
        print(f"{x}*{i}={x*i}")
main()           