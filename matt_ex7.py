#write a program that asks for user's age and prints out every number leading up to it on a new line

print("What is your age?")

answer = int(input())

for x in range(1, answer + 1):
    print(x)

