# F = 9/5 * C + 32
#write a program that asks for a temperature in C and gives it in F
#pull the printing out of the function and just do the computation

def temp_conversion(degrees_in_celsius):
    return (9 / 5 * answer + 32)

print("Give a temperature in Celsius")
answer = int(input())

print("The temperature in Fahrenheit is %f" % temp_conversion(answer))
