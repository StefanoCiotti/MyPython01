# list comprehension form = [item for item in range()]
example = [item for item in range(1, 10, 2)]

# ex1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ex1 = [num1 + 1 for num1 in range(10)]
# ex2 = [3, 6, 9, 12]
ex2 = [num2 * 3 for num2 in range(1, 5)]
# ex3 = [2, 4, 6, 8, 10]
ex3 = [num3 for num3 in range(2, 12, 2)]

# ex1 = [0, 2, 4, 6, 8]
ex1 = [num1 for num1 in range(10) if num1 % 2 == 0]
# ex2 = [0, 15, 30, 45, 60, 75, 90]
ex2 = [num2 for num2 in range(0, 99, 3) if num2 % 3 == 0 and num2 % 5 == 0]
# ex3 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
ex3 = [num3 for num3 in range(1, 21) if num3 > 10]

