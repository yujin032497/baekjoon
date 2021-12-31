#2021-12-31
#피보나치 수 5
def fac(n):
    if n<2:
        return n
    return fac(n-1)+fac(n-2)
n=int(input())
print(fac(n))
