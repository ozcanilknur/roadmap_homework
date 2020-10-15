import math

def cube(number) :
    return math.pow(number , 3)

def  by_three(number) :
    if number%3 == 0 :
        return (int(cube(number)))
    else :
        return False


print(by_three(3))

print(by_three(2))