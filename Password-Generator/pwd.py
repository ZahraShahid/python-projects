import random

print("XYZ PASSWORD GENERATOR")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*(),.?0123456789"

number = int(input("Enter the number of passwords you want to generate: "))

length = int(input("Enter the length of your password/s: "))

print("\nYOUR PASSWORDS: ")

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(chars)

    print(password)
