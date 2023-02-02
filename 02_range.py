# 1 - null
print(list(range(0)))
#[]

# 2 - stop
print(list(range(10)))
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3 - start, stop
print(list(range(5, 10)))
#[5, 6, 7, 8, 9]

# 4 - start, stop, step
print(list(range(0, 10, 2)))
#[0, 2, 4, 6, 8]

# 5 - start, stop, step (negative)
print(list(range(2, -14, -2)))
#[2, 0, -2, -4, -6, -8, -10, -12]

# 6 - float
#print(list(range(0, 1, 0.1)))
#TypeError: 'float' object cannot be interpreted as an integer

# 7 - string
#print(list(range("Hello", "World")))
#TypeError: 'str' object cannot be interpreted as an integer