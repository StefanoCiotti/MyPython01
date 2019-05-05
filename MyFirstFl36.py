counter = 0
while counter < 5:
    print("something", counter)
    counter += 1

# closed loop
counter = 1
while counter < 6:
    print(counter)
    counter += 1

counter = 1
while True:
    print("Here's Johnny!")
    counter += 1
    if counter > 5:
        break

counter = 1
while counter < 5:
    print(counter)
    counter += 1
else:
    print(5)


