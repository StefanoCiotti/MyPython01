import random;
print(random.randint(5,10))

from random import randint;
print(randint(10, 20))


from random import *;
print(random())


# ---------------
from random import *;
from random import randint;
from math import *;

print(factorial(8))



# ---------------
ex1 = abs(-3) #  ex1 is assigned the value 3
ex2 = abs(9)  # ex2 is assigned the value 9
ex3 = abs(0)  # ex3 is assigned the value 0
ex4 = abs(-5)  # ex4 is assigned the value 5

print("abs", ex1, ex2, ex3, ex4)

ex1 = type(1) # int
ex2 = type(3.21) # float
ex3 = type("example") # string
ex4 = type(True) # bool

# prints <class 'int'> <class 'float'> <class 'str'> <class 'bool'>
print("type", ex1, ex2, ex3, ex4)


ex1 = max(3, 9, 7, 13) # assigns 13 to ex1
ex2 = max(1.32, 5.6, 92.1, 4) # assigns 92.1 to ex2
ex3 = max("a", "z", "b", "t") # assigns "z" to the variable ex3
ex4 = max("ac", "ab", "az") # assigns "az" to the variable ex4
print("max", ex1, ex2, ex3, ex4)

ex1 = min(3, 9, 7, 13) # assigns 3 to ex1
ex2 = min(1.32, 5.6, 92.1, 4) # assigns 1.32 to ex2
ex3 = min("a", "z", "b", "t") # assigns "a" to the variable ex3
ex4 = min("ac", "ab", "az") # assigns "ab" to the variable ex4
print("min", ex1, ex2, ex3, ex4)


