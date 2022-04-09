import re

def wrapper(f):
    numbers = ['9876543210', '07895461230', '9195969878']


    for i in numbers:
        if len(i) == 10:
            
        x = re.findall('\?[0|+91|91]', i)
        print(x)


def fun(l):
    ret = f()
    return ret + "91"

decorated = wrapper(fun)