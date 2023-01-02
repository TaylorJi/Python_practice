# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

#input
# name = input("What is your name? ")
# print("hello " + name) #String Concatenation
#
# birth_year = input("Enter your birth year: ")
# age = 2022 - int(birth_year)
# print(age)

#simple calculator logic
# firstInput = input("Enter first number: ")
# secondInput = input("Enter second number: ")
# result = float(firstInput) + float(secondInput)
# print("result is " + str(result)) # unlike Java, there is no automatic concatenation

course = "Python 4 beginners"

print('Python' in course)

# pyhton logical operation
# and, or, not
price = 35
print(price >= 25 or price < 10)

if price == 25:
    print("The price is: " + str(price))
else:
    print("The price is not 25")


#weight converter
user_weight = input("Enter your weight: ")
weight_measure = input("(K)g or (L)bs: ")
upper_user_input = weight_measure.upper()

if upper_user_input == 'L':
    measure_kg = float(user_weight) * 2.20462
    print("user weight in found is: " + str(measure_kg))
elif upper_user_input == 'K':
    measure_lbs = float(user_weight) * 0.453592
    print("user weight in found is: " + str(measure_lbs))
else:
    print("Please check your inputs")








