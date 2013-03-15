#write a program that asks for user's age and prints out every number leading up to it on a new line
#do the same thing but add a function that does something

def user_age(number):
    print("What is your age?")

print("How old are you?")

answer = int(input())

for x in range(1, answer + 1):
    print(x)

