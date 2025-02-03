numbers = [10, 20, 4, 45, 99, 69, 45,45, 99, 69, 45, 3]

unique_numbers = sorted(set(numbers), reverse=True)
second_highest = unique_numbers[1]
print("The second highest number is:", second_highest)
