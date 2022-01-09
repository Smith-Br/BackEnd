#? Functions and Loops:
#! Functions are the building blocks of almost every Python program. They're where the real action takes place!.

# $ Functions break code into smaller chunks, and are great for tasks that a program need to perform the task, just call the function!

###? What's functions.

##! 6.1: What's a Function.
#* Functions Are Values.

##! Example:
#? In IDLE's interactive window, inspect the name len by typing the following in at the prompt:
print(len)          ##$ <build-in function len>.
print(type(len))    ##$ <class 'builtin_function_or_method>.

#$ Like any other variable, you can assign any value you want to len:
len = 'The quick brown fox jumps over the lazy dog.'
print(len, type(len))

###! If you typed in the previous code eg., you no longer have access to the built-in len function in IDLE.

##$ You can get back with the following code:

del len

#@ now you can get built-in len function:
print(len, type(len))

###! How Python Executes Functions

##$ The process for executing a function can be summarized in three steps:
    #^ 1. The function is called, and any arguments are passed to the function as input.
    #^ 2. The function executes, and some action is performed with the arguments.
    #^ 3. The function returns, and the original function call is replaced with the return value.    

random_letter_length = len("Smith Brian")
print(random_letter_length)

print_function = print("Smith Brian")
print_function #$ return nothing.

##! print() returns a special value called None that indicates the absence of date. None has a type called NoneType:

##! Write Own Function: