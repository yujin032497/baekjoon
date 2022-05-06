# 2022-05-06
# 소수&팰린드롬
import sys
from math import sqrt

def isPrime( n ): # 소수를 구하는 함수
    for j in range(2, int(sqrt(n))+1):
        if n % j == 0:
            return False # 소수가 아니면 False
    return True

n = int(sys.stdin.readline().rstrip())

for i in range(n, 1000001): # 1000000까지 이므로
    if i == 1: continue # 1은 소수가 아니므로 패스
    if i == 1000000:
        print(1003001) # 1000000의 소수는 1003001
        break
    s = str(i)
    if s == s[::-1]:
        result = isPrime(i)
        if result: # 소수이면
            print(i) # 해당 i를 출력(입력값이상의 소수이면서 팰린드롬인 최소 숫자)
            break



