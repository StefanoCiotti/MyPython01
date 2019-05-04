print("Hi all")
varDiff = 5 - 2
varDiv = 5 / 2

print(varDiff, "\n", varDiv)

str1 = 'This is a string'
str2 = '1984!'
str3 = 'rude & not ginger'
str4 = "LiVe LONG and PRosPEr."
str5 = "!@#$%^&*()_-+=/.,?><:;~`|][}{"
str6 = ""

print(str1, "\n", str2, "\n", str3, "\n", str4, "\n", str5, "\n", str6)
# prints lower as output
# prints UPPER as output
str1 = "mySTRING_string"
print(str1.lower())
print(str1.upper())


example = "apples"
ex1 = example[:3]  # assign the string "app" to the variable ex1
ex2 = example[2:5]  # assign the string "ple" to the variable ex2
ex3 = example[3:]  # assign the string "les" to the variable ex3

ex4 = "apples"[:3]  # assign the string "app" to the variable ex4
ex5 = "apples"[2:5]  # assign the string "ple" to the variable ex5
ex6 = "apples"[3:]  # assign the string "les" to the variable ex6

print("\n", ex1, "\n", ex2, "\n", ex3, "\n", ex4, "\n", ex5, "\n", ex6)


string = "Yoda"  # we will use the -len()- method on this string.
length = len(string)  # assigns the number of characters in the string "Yoda" to the variable length
print("Yoga is", length, "long")  # prints the number of characters in the string "Yoda", which is 4


print(len("Manchester United"))
print(str(12345)[2])
print("albania".upper())
print("BELGIUM".lower())


str1 = "example1"
num = 7
print(str1)  # outputs example1 when the code is run
print(num)  # outputs 7 when the code is run
print("example2")  # outputs example2 when the code is run
print(9)  # outputs 9 when the code is run


print("word1 " + "word2 " + "word3")  # outputs string "word1 word2 word3"
print("R" + str(2) + "-D" + str(2))  # outputs string “R2-D2”

city = "Seattle"
state = "Washington"  # the line below outputs the string "The Seahawks are from Seattle, Washington."
print("The Seahawks are from %s, %s." % (city, state))


occupation = input("What is your occupation?")
city = input("What city do you live in?")
age = input("How many years old are you?")

# occupation = "What is your occupation?"
# city = "What city do you live in?"
# age = "How many years old are you?"

print("So you are a %s, you live in %s, and you are %s years old." % (occupation, city, age))

ex1 = 3 > 1  # ex1 = True
ex2 = 5 >= 5  # ex2 = True
ex3 = 3 < 3  # ex3 = False
ex4 = 7 <= 6  # ex4 = False
ex5 = 1 == 7  # ex5 = False
ex6 = 8 != 8  # ex6 = False
print("\n", ex1, "\n", ex2, "\n", ex3, "\n", ex4, "\n", ex5, "\n", ex6)


ex1 = True and True  # ex1 = True
ex2 = True and False  # ex2 = False
ex3 = False and False  # ex3 = False
ex4 = True or True  # ex4 = True
ex5 = True or False  # ex5 = True
ex6 = False or False  # ex6 = False
ex7 = not True  # ex7 = False
ex8 = not False  # ex8 = True
print("\n", ex1, "\n", ex2, "\n", ex3, "\n", ex4, "\n", ex5, "\n", ex6, "\n", ex7, "\n", ex8)


if 1 == 2:
    print("1 equals 2.")
else:
    print("1 does not equal 2!")


if 1 == 2:
    print("Don't print this.")
elif 1 != 2:
    print("Print this.")
else:
    print("Don't print this either.")


if 1 == 2:
    print("Don't print this.")
elif 1 != 1:
    print("Don't print this either.")
elif 5 <= 19:
    print("2nd elif statement.")
else:
    print("This will not be printed.")

