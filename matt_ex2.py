#write a program that asks for user's age and tells you how old user will be in 30 years and must include a function

def user_age(number):
    return (number + 30)

print("What is your age?")

answer = int(input())

print("In thirty years you will be %d" % user_age(answer))
