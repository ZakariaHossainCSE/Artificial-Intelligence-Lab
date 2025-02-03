numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_even = 0
sum_odd = 0
for num in numbers:
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num

print("Sum of even numbers:", sum_even)
print("Sum of odd numbers:", sum_odd)
