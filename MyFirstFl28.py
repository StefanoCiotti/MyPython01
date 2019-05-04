# tupleForm = 1st, 2nd, 3rd, etc
# tupleForm = (1st, 2nd, 3rd, etc)
tuple1 = (5.6, "California", True, 1)
tuple2 = 7, "Star Trek", 9.92, False
empTup = () # empty tuple

# assign a tuple to tupEx
tupEx = (1, 2, 3, 4, 5)

# accessing by index
print(tupEx[1]) # prints 2
print(tupEx[3]) # prints 4

# tuple slicing
first3 = tupEx[:3] # prints (1, 2, 3)
mid3 = tupEx[1:4] # prints (2, 3, 4)
last3 = tupEx[2:] # prints (3, 4, 5)

list1 = [1, 2, 3]
tuple1 = (4, 5, 6)

# iterate through list
for elements in list1:
    print(elements)

# iterate through tuple
for items in tuple1:
    print(items)

# list
list1 = [4, 3, 2, 1, 0]
empty = []

# tuple
tup = ("Let ", "It ", "Be")
song = ""

# after this for loop, empty = [16, 12, 8, 4, 0]
for nums in list1:
    empty.append(nums * 4)

# after this for loop, song = "Let It Be"
for words in tup:
    song += words

print(empty) # prints [16, 12, 8, 4, 0]
print(song) # prints Let It Be

