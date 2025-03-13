# Write a Python program to check for access to a specified path. 
# Test the existence, readability, writability and executability of the specified path
import os
path = r"C:\Users\erbat\OneDrive\Desktop\GitHub\PP2\Labs\Lab6\DirFiles\test_file.txt"
if os.path.exists(path):
    print(f"Путь существует: {path}")
    print(f"Читаемый: {'Да' if os.access(path, os.R_OK) else 'Нет'}")
    print(f"Записываемый: {'Да' if os.access(path, os.W_OK) else 'Нет'}")
    print(f"Исполняемый: {'Да' if os.access(path, os.X_OK) else 'Нет'}")
else:
    print(f"Путь не существует: {path}")

    