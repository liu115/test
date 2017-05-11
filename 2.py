
def count(x):
    total = 0
    for i in range(x):
        if (i+1) % 15 == 0:
            total += 1
        elif (i+1) % 3 != 0 and (i+1) % 5 != 0:
            total += 1
    return total


print(count(15))

