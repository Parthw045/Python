fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original:", fruits)

fruits.append("Grapes")
print("Append:", fruits)

fruits.insert(1, "Watermelon")
print("Insert:", fruits)

fruits.remove("Banana")
print("Remove:", fruits)

print("Length:", len(fruits))

print("Index of Mango:", fruits.index("Mango"))

print("Count of Mango:", fruits.count("Mango"))

fruits.sort()
print("Sorted:", fruits)

fruits.reverse()
print("Reversed:", fruits)

fruits.pop(2)
print("After pop:", fruits)

new_fruits = fruits.copy()
print("Copied List:", new_fruits)

new_fruits.clear()
print("After clear:", new_fruits)