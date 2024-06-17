# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input

temp = input("Enter the temperature you want to convert: ")
tem = temp[-1]
degree = int(temp[:-1])
if tem.upper() == "C":
    result = (9*degree + (32*5))/5
    print(temp, "in degree celsius is", result,"F")
elif tem.upper() == "F":
    result = (degree - 32)*(5/9)
    print(temp, "in degree Fahrenheit is", result,"C" )
else:
    print("Enter valid value")


