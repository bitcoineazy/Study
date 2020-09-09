a = int(input())
b = int(input())
c = int(input())
def printMath():
    p = a + b + c
    print(max(a,b,c))
    print(min(a,b,c))
    print(p - max(a,b,c) - min(a,b,c))
printMath()

