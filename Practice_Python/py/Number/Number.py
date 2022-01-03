# 5.1 Integers and Floating-Point Numbers.
# Integers
print(type(1))
print(type(1.0))  # ! isn't integers. It's float.
int("25")  # ? it'll print 25.
# Integer literals can be written in two different ways:
print(1000000)
print(1_000_000)

# Floating-Point Numbers
print(type(1.0))
print(float("3.14"))
print(1e6)
print(1e+9)  # ! we can use E-notations for really large number.
# we also can use 'e-'.
print(1e-6)
print(9e-9)
# ? the number have "E-notations" always is float.

#! multiplication
#* if multiply two number (int * float) = <float>
print(1 * 1.0)  # <float>

#! division
#* if division two number (int / float) = <float>
print(1.0 / 1)  # <float>

#! couldn't divide by 0

#! integer division
print(3 // 2)
print(5 // 2)

# Exponents
print(2 ** 4)  # 2^4
#! float also correct:
print(2 ** 1.5)

#TODO Math function
# round(): ≈.
# abs(): |x|.
# pow(): x^a.

print(round(3.14156))  # round(): ≈.
print(abs(-1))  # abs(): |x|.
print(pow(2, 4))
print(pow(2, -4))  # pow(): x^a.

#! round(a, b)  - b is the given number of decimal places by passing a second argument to round().
print(round(3.1415, 2))

#! pow(x, y, z) = (x ** y) % z.
print(pow(1, 2, 3))

#! Check if a Float Is Integral:
#$ we can use .isinteger():
def test_num():
    number = 3.14156
    float = 1.0    #// not 1.
    print(number.is_integer(), float.is_integer())
test_num()

##! Print Numbers in Style.
rannum = 3.14156; print(f"The value of rannum is {rannum}") #@ f"sth{num}".
print(f"The value of rannum is {rannum:.2f}") #! = equal to round(3.14156, 2)

test_num1 = .5; test_num2 = .56; print(f"The value of rannum is {test_num1:.1f}"); print(f"The value of rannum is {test_num2:.1f}")

#@ display currency values:
number = 1234.5678
print(f"The value of number is {number:,.2f}")

#@ Ratio
ratio = 0.9; print(f"Over {ratio:%} of pythonistas say 'Real Python rocks'"); print(f"Over {ratio:.1%} of pythonistas say 'Real Python rocks'"); print(f"Over {ratio:.2%} of Pythonnistas say 'Real Python rocks'")

###! Complex numbers.
complex_number = 1 + 1j; print(complex_number) #$ The conclusion we have (1+1j)
#$ We also call .real and .imag to return a real - imaginary component of the number:
print(complex_number.real, complex_number.imag); print(complex_number.conjugate()) #$ return negative value of the complex_number.
print((1 - 2j).conjugate())

##^ Complex arithmetic
def complex_arithmetic():
    n1 = 1j
    n2 = 2 + 1j
    n3 = 3 - 12j
    print(n1 + n2, n3 / n1, n3 - n1, n3 ** n2 ** n1)
complex_arithmetic()

#@ Interestingly, although not surprising from a mathematical point of view, int and float objects also have the .real and .imag properties, as well as the .conjugate() method:

number_1 = 3.14156; print(number_1.real, number_1.imag, number_1.conjugate())
# With int. the .imag always return '0' value.