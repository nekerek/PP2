# Write a Python program to list only directories, files and all directories, 
# files in a specified path.
import os
path=r"C:\Users\erbat\OneDrive\Desktop\GitHub\PP2\Labs\Lab6\DirFiles"
all_items = os.listdir(path)
print(all_items)