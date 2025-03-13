print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

# You can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello, World!"
print(a[1])

# Loop through the letters in the word "banana":
for x in "banana":
  print(x)

# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)

# Print only if "free" is present:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)

# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


# Slicing
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])
# Get the characters from the start to position 5 (not included):
print(b[:5])
# Get the characters from position 2, and all the way to the end:
print(b[2:])
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
print(b[-5:-2])


# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
# The lower() method returns the string in lower case:
print(a.lower())
# The replace() method replaces a string with another string:
print(a.replace("H", "J"))
# The split() method splits the string into substrings if it finds instances of the separator:
print(a.split(",")) # returns ['Hello', ' World!']
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#Concatenation

# Merge variable a with variable b into variable c:
a = "Hello"
b = "World"
c = a + b
print(c)
# To add a space between them, add a " ":
c = a + " " + b
print(c)

# Create an f-string:
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# Add a placeholder for the price variable:
price = 59
txt = f"The price is {price} dollars"
print(txt)
# Display the price with 2 decimals:
txt = f"The price is {price:.2f} dollars"
print(txt)

# Perform a math operation in the placeholder, and return the result:
txt = f"The price is {20 * 59} dollars"
print(txt)

# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."

txt = 'It\'s alright.'
print(txt) 
txt = "This will insert one \\ (backslash)."
print(txt) 
txt = "Hello\nWorld!"
print(txt) 
txt = "Hello\rWorld!"
print(txt) 
txt = "Hello\tWorld!"
print(txt) 
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
