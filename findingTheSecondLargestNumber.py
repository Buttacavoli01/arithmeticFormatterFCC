if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(set(arr))[-2])

    #n accepts numbers
    #arr turns those numbers into a map, which is iterable
    #sorting, then turning the map into a set object and
    #then returning the second to last value



    # Python program to demonstrate working
    # of map.

    # # Return double of n
    # def addition(n):
    #     return n + n
    #
    #
    # # We double all numbers using map()
    # numbers = (1, 2, 3, 4)
    # result = map(addition, numbers)
    # print(list(result))