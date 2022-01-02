##! Challenge: perform Calculations on User Input.
base = int(input("Enter a base: ")); exponent = int(input("Enter a exponent: "))
print(str(base) + " to the power of " + str(exponent) + " = " + str(pow(base, exponent)))

#^ 1. Write a script that asks the user to input a number and then displays that number rounded to two decimal places.

user_input_number = float(input("Enter a number: "))
print(str(user_input_number) + " rounded to 2 decimal places is " + str(round(user_input_number)))

#^ 2. Write a script that asks the user to input a number and then displays the absolute value of that number.

input_ex_2 = int(input("Enter a number: "))
print("The absolute value of " + str(input_ex_2) + " is " + str(abs(input_ex_2)))

#^ 3. Write a script that asks the user to input two numbers by using the input() function twice, then display whether or not the difference between those two number is an integer.

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
if num1.is_integer and num2.is_integer == 1:
    print("The difference between " + str(num1) + " and " + str(num2) + " is an integer? True!")
else:
    print("The difference between " + str(num1) + " and " + str(num2) + " is an integer? False!")