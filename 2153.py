# 2022-05-06
# 소수 단어
import sys
from math import sqrt

# 소수구하기
def isPrime(num):
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            return 'It is not a prime word.' # 소수가 아니면
    return 'It is a prime word.' # 소수이면

# 알파벳
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

s = list(sys.stdin.readline().rstrip())
n = 0

for i in s:
    n += (alphabet.index(i)+1) # 알파벳 숫자 더하기
print(isPrime(n)) 
