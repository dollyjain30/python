# Lists
# Lists are ordered, mutable (changeable) collections of items.

# Creating a List:
# numbers = [1, 2, 3, 4, 5]
# mixed = [10, "hello", 3.14]
# my_list = [1, 2, 3]
 
# my_list.append(4)   # [1, 2, 3, 4]
# my_list.insert(1, 99)  # [1, 99, 2, 3, 4]
# my_list.remove(2)   # [1, 99, 3, 4]
# my_list.pop()       # Removes last element -> [1, 99, 3]
# my_list.reverse()   # [3, 99, 1]
# my_list.sort()      # [1, 3, 99]
# print(my_list)
x=[3,5,3,2,7,9]
s=[i** 2 for i in x]
s.remove(49)
print(s)
#list changes the original list
