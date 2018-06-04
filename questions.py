# """
# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between
#    1500 and 2700 (both included).
# """
# numbers = range(1500,2700)
# print("This is the first number {}".format(numbers[1]))
# print("This is the second number {}".format(numbers[2]))
#
# n = []
# for item in numbers:
#     if item % 7 == 0:
#         if item % 5 == 0:
#             n.append(item)
# print(n)

"""
2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
    [ Formula : c/5 = f-32/9 ]
Expected Output :
      60°C is 140 in Fahrenheit
      45°F is 7 in Celsiu
Note: The provided solution used a user input although it did not ask for one.
      I added a feature that would ask the user if they wanted to try again if the
      wrong format was used or if they wanted to convert more than one temperature.
"""
while True:
    degree = chr(176) #code for using degree symbol
    temp = input("Please enter a tempature followed by C for celsius or F for fahrenheit:  ")

    if temp[-1].upper() == "F":
        temp = int((temp[:-1]))
        fahrenheit = int(((temp - 32) / 9) * 5)
        print(str(temp) + degree + "F is " + str(fahrenheit) + degree + " in Celsius")
    elif temp[-1].upper() == "C":
        temp = int((temp[:-1]))
        celsius = int(((temp / 5) * 9) + 32)
        print(str(temp) + degree + "C is " + str(celsius) + degree + " in Fahrenheit")
    else:
        print("Please enter the number followed by C for celsius or F for fahrenheit (Example: 36c)")
    again = (input("Would you like to try again? y/n:  ")).upper()

    if again.startswith('Y'):
        continue
    elif again.startswith('N'):
        exit()
    else:
        continue
#need to raise error if something is input other than y or n


