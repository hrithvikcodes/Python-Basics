print("Hello!")
name= input("What's your name?")

#name= name.strip() #removes whitespace from str
#name=name.capitalize() #used to convert the first character of a string to uppercase and the rest to lowercase.


#name=name.title()  #converts the first character of each word to uppercase and the rest to lowercase.

name=name.strip().title()
print(f'Welcome, '+name)