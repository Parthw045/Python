
fruits = ("Apple", "Banana", "Mango", "Orange", "Mango")

print("Original Tuple:", fruits)

print("Length:", len(fruits))

print("Index of Mango:", fruits.index("Mango"))

print("Count of Mango:", fruits.count("Mango"))

print("First element:", fruits[0])
print("Last element:", fruits[-1])

print("First three elements:", fruits[0:3])

print("Is Banana present?", "Banana" in fruits)

vegetables = ("Potato", "Tomato")
combined = fruits + vegetables
print("Combined Tuple:", combined)

numbers = (1, 2, 3)
print("Repeated Tuple:", numbers * 2)

fruit_list = list(fruits)
print("Tuple converted to List:", fruit_list)

new_tuple = tuple(fruit_list)
print("List converted to Tuple:", new_tuple)