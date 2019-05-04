example1 = ["eggs", 1, "spam", 7.96]
example2 = ["green", "yellow", "blue"]
example3 = [] # empty list

# accByIndex = nameOfList[index of value accessed]
byIndex = ["green", "eggs", "and", "ham"]
# ham = "ham"
ham = byIndex[3]
# greenEggs = "green eggs"
greenEggs = byIndex[0] + " " + byIndex[1]

reAssign = [1, 1, 3, 8]
# re-assigns reAssign[2] the value 5
reAssign[2] = 5
# now, reAssign = [1, 1, 5, 8]

# nameOfList.append(value)
adder = [1, 2, 3, 4]
# appends 5 to the end of adder
adder.append(5)
# now, adder = [1, 2, 3, 4, 5]


sliceEx = [9, 0, 2, 1, 0]
# slice1 = [9, 0]
slice1 = sliceEx[:2]
# slice2 = [2, 1]
slice2 = sliceEx[2:4]
# slice3 = [0, 2, 1, 0]
slice3 = sliceEx[1:]


indexed = [0, 1, 0, 1, 1]
# firstZero = 0
firstZero = indexed.index(0)

inserted = ["Through", "Looking", "Glass"]
# inserts "the" at index 1 of inserted
inserted.insert(1, "the")
# now, inserted = ["Through", "the", "Looking", "Glass"]

removed = ["Ned Stark", "Catelyn Stark", "Tony Stark", "Bran Stark"]
# removes "Tony Stark" from removed
removed.remove("Tony Stark")
# now, removed = ["Ned Stark", "Catelyn Stark", "Bran Stark"]

popped = ["Foo Fighters", "Nirvana", "Green Day", "The White Stripes"]
# removes "Green Day" from popped and assigns it to a variable
noDaveGrohl1 = popped.pop(2)
# now, popped = ["Foo Fighters", "Nirvana", "The White Stripes"]
# removes "The White Stripes" from popped and assigns it to a variable
noDaveGrohl2 = popped.pop()
# now, popped = ["Foo Fighters", "Nirvana"]
