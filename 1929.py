# 2022-01-25
# 소수 구하기
import math
n,m=map(int,input().split()) # 두 수를 받는다
t=[True]*(m+1) # 두 번째 수 만큼 True 배열을 만든다
a=int(math.sqrt(m)) # 두 번째 수의 제곱근
for i in range(2,a+1): # 2부터 제곱근만큼 반복(2부터 소수 시작)
  for j in range(i,m+1,i): # i만큼 +i(배수) m까지
    if i==j: # 자기자신이면 건너뛰고
      continue
    else: # 아니면 False (배수!=소수)
      t[j]=False
for k in range(n,m+1): # 1보다 크고 True인 경우만(True = 소수)
  if k>1 and t[k]==True:
    print(k)
