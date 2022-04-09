def high_and_low(numbers):
    spl = numbers.split()
    newList = []

    for i in spl:
        newList.append(int(i))

    high = max(newList)
    low = min(newList)

    return str(high) + " " + str(low)

high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")