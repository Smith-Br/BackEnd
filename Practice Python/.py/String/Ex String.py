# 1. Print a string that uses double quotation marks inside the string.
print('"I want a hot water" - he said')

# 2. Print a string that uses an apostrophe: nháy đơn. inside the string.
print("\"I'm a developer\" - He said")

# 3. Print a string that spans multiple lines, with whitespace preserved.
print('''The quick brown fox jumps over the lazy dog.''')

# 4. Print a string that is coded on multiple lines but displays on a single line.
print(
    'The quick brown fox jumps over the \
lazy dog.'
    )

### 4.3
def Ex4_3():
# 1. Create a string and print its length using the len() function.
    string = "The quick brown fox jumps over the lazy dog."
    print(len(string))

# 2. Create two strings, concatenate them, and print the resulting string.
    str_1 = "The quick brown fox jumps "
    str_2 = "over the lazy dog."
    print(str_1 + str_2)

# 3. Create two strings and use concatenation to add a space inbetween them. Then print the result.
    Str_1 = "The quick brown fox jumps"
    Str_2 = "over the lazy dog."
    print(Str_1 + " " + Str_2)

Ex4_3()