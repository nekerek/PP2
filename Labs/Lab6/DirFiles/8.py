# Write a Python program to delete file by specified path. 
# Before deleting check for access and whether a given path exists or not.
import os
file_path = input("Введите путь к файлу: ")

if not os.path.exists(file_path):
    print(f"Файл '{file_path}' не существует.")

elif not os.access(file_path, os.W_OK):
    print(f"Нет доступа для удаления файла '{file_path}'.")

else:
    os.remove(file_path)
    print(f"Файл '{file_path}' удалён.")