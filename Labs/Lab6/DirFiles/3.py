# Write a Python program to test whether a given path exists or not. 
# If the path exist find the filename and directory portion of the given path.
import os
path = r"C:\Users\Kazbek\Documents\Academic Materials of KBTU\PP2 codes\lab6\Built-in funcs\4.py"  
if os.path.exists(path):
    print(f"Путь существует: {path}")
    filename = os.path.basename(path)
    print(f"Имя файла: {filename}")

    directory = os.path.dirname(path)
    print(f"Папка: {directory}")
else:
    print("Путь не существует.")
