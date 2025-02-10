
input_numbers = input("Enter numbers: ")

numbers = list(map(int, input_numbers.split()))

unique_sorted = sorted(set(numbers))

print("Unique sorted list:", unique_sorted)