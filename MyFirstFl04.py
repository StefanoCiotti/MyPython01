def ex():
  print("hello world")
ex()

def single(a):
  print(a)
single(9)

def mult(a, b, c):
  d = a * b
  print(d + c)

mult(2, 3, 4)

def giver(a, b):
  c = a + b
  return c

def taker(d, e):
  output = giver(d, e)
  return output

print(taker(1, 5))

# --------------

def first():
  print("This is a funcion")

def intFun(intVal):
  return intVal*2

def takesTwo(int1, int2):
  return int1*int2

def functionInside(a,b,c):
  print(takesTwo(intFun(a),b) *c)

first()
functionInside(7,4,2)
