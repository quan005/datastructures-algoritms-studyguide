# intializing an Array
import array as arr

array = arr.array('i', [1, 2, 3, 4, 5])

print(array)

# ---- Array Operations ----

# Traverse
for i in array:
    print(i)


# Insert
array.append(6)
print(array)

array.extend([7,8,9])
print(array)


# Delete
del array[3]
print(array)

array.remove(8)
print(array)

array.pop(2)
print(array)

# Search
found = array.index(9)
print(found)

# Update
array[5] = 11
print(array)

array[1:4] = arr.array('i', [11, 12, 43])
print(array)




# A List is also an array type data structure in python
# with the difference being that it can contain elements
# of different types such as strings, booleans, etc. all at once

# intializing a List
list = [1, 2, 3, 4, 5, 6]
print(list)

# Traverse
for x in list:
    print(x)

# Insert
list.append(7)
print(list)

list.extend([8, 9, 10, 11])
print(list)

# Delete
del list[3]
print(list)

list.remove(8)
print(list)

list.pop(3)
print(list)

# Search
search = list.index(9)
print(search)
print(list[search])

# Update
list[5] = 11
print(list)