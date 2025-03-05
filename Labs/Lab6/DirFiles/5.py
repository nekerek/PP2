# Write a Python program to write a list to a file.
file_path=r"Labs/Lab6/DirFiles/write_a_list.txt"
array=["123","QWERTY","095"]

with open(file_path,"w") as file:
    for item in array:
        file.write(item+" ")