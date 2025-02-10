list1 = input("Enter first list of numbers: ").split()
list2 = input("Enter second list of numbers: ").split()
common_elements = set(list1) & set(list2)
print(common_elements)