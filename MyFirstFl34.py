exList = [1, 2, 3, 4, 5]
def print_items(a):
    for items in a:
        print(items)
print_items(exList)

# range(stop)
var1 = range(8) # [0, 1, 2, 3, 4, 5, 6, 7]
# range(start, stop)
var2 = range(1, 4) # [1, 2, 3]
# range(start, stop, step)
var3 = range(2, 20, 3) # [2, 5, 8, 11, 14, 17]

# range(stop)
var1 = range(5) # [0, 1, 2, 3, 4]
def passed(x):
    return(x)
# prints range(0, 5)
print(passed(var1))

exList = [1, 5, 9, 13]
def iterator(a):
    for x in range(0, len(a)):
        print(a[x])
iterator(exList)

exList = [1, 3, 5, 7, 9]
def modifier(a):
    for item in range(0, len(a)):
        a[item] *= 2
    return a
# prints [2, 6, 10, 14, 18]
print(modifier(exList))


list1 = [1, 3, 5]
list2 = [2, 4, 6]
def multiList(a, b):
    print(a, b)
multiList(list1, list2)

listOfLists = [[1, 3, 4], [2, 5, 6]]
def makeOneList(a):
    bothLists = []
    for item in a:
        for element in item:
            bothLists.append(element)
    print(bothLists)
# prints [1, 3, 4, 2, 5, 6]
makeOneList(listOfLists)

