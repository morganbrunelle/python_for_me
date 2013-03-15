#write a program that asks the user for how many miles they ran that day and tells them how many km they ran
# 1 mile = 1.6 km

def miles_to_km(miles):
    return (answer * 1.6)

print("How many miles did you run today?")

answer = int(input())

print("The amount of kilometers you ran today was %f" % miles_to_km(answer))
