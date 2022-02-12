def convert_cel_to_far(C):
    print("C --> F = " + str(C * 9/5 + 32))
convert_cel_to_far(float(input("Your Celcius degrees: ")))


def convert_far_to_cel(F):
    print("D --> C = " + str((F - 32) * 5/9))
convert_far_to_cel(float(input("Your Fahrenheit degrees: ")))

