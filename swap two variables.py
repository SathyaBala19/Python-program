a = input("Enter the value of first variable (a): ")
b = input("Enter the value of second variable (b): ")

print(f"The original values: a = {a}, b = {b}")

temp = a
a = b
b = temp

print(f"Swapped values: (a) = {a}, (b) = {b}")