# format string
def format():
    string = "Smith Brian"
    print(string.upper())
    print(string.isupper())
    print(string.upper().isupper())
format()

# determine length of string: len()
def checks():
    print(len("The quick brown fox jumps over the lazy dog"))
    lens = "Lorem Ipsum"
    print(len(lens))
checks()
 
### 4.2 Concatenation, Indexing, and Slicing.

## String concatenation.
str_1 = 'The quick brown fox jumps '
str_2 = 'over the lazy dog.'
print(str_1 + str_2)

## String index.
    # Đếm xuôi từ 0 nhưng đếm nhưng đếm ngược từ -1.
def str_index():
    str = "Smith Brian"
    print(str[0], str[-1], str[0:], str[:-1])

    #! index() - determine the location of string.
    print(str.index("i")) #* It'll count from left to right, count 1 value.
    print(str.index("Smith")) #* It started from...

    #! lstrip() - remove the whitespace in the left - the same as rstrip().
    strip = "    Smith Brian    "
    rstrip = "Smith Brian    "
    lstrip = "    Smith Brian"
    print(rstrip.rstrip()); print(lstrip.lstrip()); print(strip.strip())

    #! replace() - replace string <replace(<root string>, <replace string>).
    print(str.replace("Smith", "Dev."))
str_index()

### Determine if a String Starts or Ends With a Particular String
def somethingelse():
    str = "The quick brown fox jumps over the lazy dog"
    print(str.startswith("The"), str.endswith("Dog"))
somethingelse()

### TODO
    ##? format()	    It’s used to create a formatted string from the template string and the supplied values.
    ##? split()	        Python string split() function is used to split a string into the list of strings based on a delimiter.
    ##? join()	        This function returns a new string that is the concatenation of the strings in iterable with string object as a delimiter.
    ##? strip()	        Used to trim whitespaces from the string object.
    ##? format_map()	Python string format_map() function returns a formatted version of the string using substitutions from the mapping provided.
    ##? upper()	        We can convert a string to uppercase in Python using str.upper() function.
    ##? lower()	        This function creates a new string in lowercase.
    ##? replace()	    Python string replace() function is used to create a new string by replacing some parts of another string.
    ##? find()	        Python String find() method is used to find the index of a substring in a string.
    ##? translate()	    Python String translate() function returns a new string with each character in the string replaced using the given translation table.
