def moon_weight(number):
    return (0.25 * number + 1)

print("What is your weight?")

number = int(input())

print("Your weight on the moon is %f" % moon_weight(number))

