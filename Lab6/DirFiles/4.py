# Write a Python program to count the number of lines in a text file.
file_path=r"C:\Users\erbat\OneDrive\Desktop\GitHub\PP2\Labs\Lab6\DirFiles\1.py"
with open(file_path,"r") as a:
    line_counter=len(a.readlines())

    
print(line_counter)