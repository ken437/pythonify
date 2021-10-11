import sys  # This should not matter

def aFunc():
    pass

def bFunc():
    pass

class A():
    def __init__(self):
        a = 1

def cFunc(arg1):
    print(arg1)
    a = [1, 2, 3]
    b = a[-1]
    c = a[len(a) - 1]

if __name__ == "__main__":
    cFunc("hi")
