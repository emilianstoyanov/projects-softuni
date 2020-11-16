file_path = "./files/demo1.py"

try:
    open(file_path, "r")
    print("File found")
except:
    print("File not found")


