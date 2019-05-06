exList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sliced1 = [1, 4, 7, 10]
sliced1 = exList[0:10:3]
# sliced2 = [2, 4, 6, 8]
sliced2 = exList[1:9:2]


exList = [1, 2, 3, 4, 5]
# omitted = [1, 3, 5]
omitted = exList[::2]
print(omitted)


exList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# var1 = [9, 7, 5, 3]
var1 = exList[8:1:-2]
print(var1)

exList = [6, 7, 8, 9, 10]
# reversed = [10, 9, 8, 7, 6]
reversed = exList[::-1]
print(reversed)



