# Read, Write, and Append Files
# Python provides several modes for opening files:

# 'r' (Read mode): Opens the file for reading. This is the default mode. If the file doesn't exist, you'll get an error.
# 'w' (Write mode): Opens the file for writing. If the file exists, its contents will be overwritten. If the file doesn't exist, a new file will be created.
# 'a' (Append mode): Opens the file for appending. Data will be added to the end of the file. If the file doesn't exist, a new file will be created.

# f = open("file.txt", "r")
# content = f.read()
# print(content)
# f.close()

# f=open("write.txt","w")
# string ='''
# hello my name is dolly jain.
# helllooo
# '''
# f.write(string)
# f.close()

f=open("write.txt","a")
string ='''
heyyyyyy
helllooo
'''
f.write(string)
f.close()