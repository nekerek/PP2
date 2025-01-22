# Upper case the first letter in this sentence:
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

# Make the string lower case:
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
txt = "banana"
x = txt.center(20)
print(x)

# Return the number of times the value "apple" appears in the string:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

# UTF-8 encode the string:
txt = "My name is Ståle"
x = txt.encode()
print(x)

# Check if the string ends with a punctuation sign (.):
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)

# Set the tab size to 2 whitespaces:
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)

# Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

# Insert the price inside the placeholder, the price should be in fixed point, two-decimal format:
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

# Check if all the characters in the text are alphanumeric:
txt = "Company12"
x = txt.isalnum()
print(x)

# Check if all the characters in the text are letters:
txt = "CompanyX"
x = txt.isalpha()
print(x)

# Check if all the characters in the text are ascii characters:
txt = "Company123"
x = txt.isascii()
print(x)

# Check if all the characters in a string are decimals (0-9):
txt = "1234"
x = txt.isdecimal()
print(x)

# Check if all the characters in the text are digits:
txt = "50800"
x = txt.isdigit()
print(x)

# Check if all the characters in the text are in lower case:
txt = "hello world!"
x = txt.islower()
print(x)

# Check if all the characters in the text are whitespaces:
txt = "   "
x = txt.isspace()
print(x)

# Check if all the characters in the text are in upper case:
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)

# Join all items in a tuple into a string, using a hash character as separator:
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

# Return a 20 characters long, left justified version of the word "banana":
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

# Search for the word "bananas", and return a tuple with three elements:
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

# Where in the text is the last occurrence of the string "casa"?:
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

# Make the lower case letters upper case and the upper case letters lower case:
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)