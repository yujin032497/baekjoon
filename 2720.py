# 2022-05-08
# 세탁소 사장 동혁
import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(1, T+1):
    
    N = int(sys.stdin.readline().rstrip())
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0
    
    while N > 0:
        
        if N >= 25: 
            quarter = N//25
            N-= 25*(N//25)
        elif N >= 10:
            dime = N//10
            N-= 10*(N//10)
        elif N >= 5:
            nickel = N//5
            N-= 5*(N//5)
        elif N >= 1:
            penny = N
            N-=N
    
    print("%d %d %d %d" %(quarter, dime, nickel, penny))
