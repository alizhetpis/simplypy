import random

# randint
print("Random integer using randint(): ", random.randint(1, 100))

# randrange
print("Random integer using randrange(): ", random.randrange(1, 101))

# random (float 0 - 1)
print("Random float using random(): ", random.random())

# enumerate
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")
