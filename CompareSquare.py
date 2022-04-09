def comp(array1, array2):
    squaredarr = []

    for i in array1:
        squaredarr.append((i * i))
    return sorted(squaredarr) == sorted(array2)


comp([121, 144, 19, 161, 19, 144, 19, 11], [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19])