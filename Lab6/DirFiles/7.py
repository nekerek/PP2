# Write a Python program to copy the contents of a file to another file
file_path=r"C:\Users\erbat\OneDrive\Desktop\GitHub\PP2\Labs\Lab6\DirFiles\write_a_list.txt"
file_copy=r"C:\Users\erbat\OneDrive\Desktop\GitHub\PP2\Labs\Lab6\DirFiles\to_copy.txt"
with open(file_path,"r") as file:
    content=file.read()
    with open(file_copy,"w") as copy:
        copy.write(content)