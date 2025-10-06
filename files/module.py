# OS and Shutil Modules in Python
# Python's os module provides functions for interacting with the operating system, such as working with directories and files. The shutil module offers higher-level file operations.
import os
#a=os.listdir("dir")#gives the list of files inside this directories
#print(a)
print(os.getcwd())
import shutil
 
# Copy a file
# shutil.copy("my_file.txt", "my_file_copy.txt")
 
# Move a file or directory
# shutil.move("my_file.txt", "new_directory/")