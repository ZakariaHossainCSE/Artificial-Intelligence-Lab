def find_largest(a, b):
    if a > b:
        return a
    else:
        return b
num1 = 10
num2 = 20
largest = find_largest(num1, num2)
print("The largest number is:", largest)