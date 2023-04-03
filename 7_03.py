phone_book = {}
n = int(input())

# Reading phone numbers and names
for i in range(n):
    phone, name = input().split()
    phone_book[name] = phone

# Reading the name to search for
name = input()

# Finding the phone number for the given name
if name in phone_book:
    print(phone_book[name])
else:
    print("Нет в телефонной книге")
