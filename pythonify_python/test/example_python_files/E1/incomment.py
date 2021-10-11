# The antipattern appears here but the code should not pick up
# on it:
# def func(param):
#     a = [1, 2]
#     a = a[len(a) - 1]

def aFunc(param1, param2, param3):
    a = [1, 2, 3, 4]
    return a[-1]

def bFunc(param1, param2, param3):
    var1 = 2
    var2 = var1 + 1

if __name__ == "__main__":
    bFunc(1, 2, 3)
