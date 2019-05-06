# Iterating Through A String Using range() And A For Loop
ex_str = "example"
for char in ex_str:
    print(char)

ex_str = "example"
for char in range(len(ex_str)):
    print(ex_str[char])


# Using “,” In A Print Statement In A For Loop
ex_str = "example"
for char in ex_str:
    print(char, end=" ")

ex_str = "example"
for char in ex_str:
    print(char, end="Z")

# Using A For Loop to Iterate Through A Dictionary
ex_dict = {"first": 1, "second": 2, "third": 3}
for key in ex_dict:
    print(key + " " + str(ex_dict[key]))

# zip()
list1 = [4, 0, 11, 3]
list2 = [1, 1, 9, 18]
for items1, items2 in zip(list1, list2):
    if items1 > items2:
        print(items1)
    elif items1 < items2:
        print(items2)