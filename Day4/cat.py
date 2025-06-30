def main():
    number= get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n<0:
            continue
        else:
            return n 

def meow(n):
    for _ in range(n):
        print("Meoww!!")
main()        
