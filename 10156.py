# 2022-01-11
# 과자
k,n,m=map(int,input().split()) # k = 과자한개가격, n = 과자의 개수 m = 현재 동수가 가진 돈
if k*n>m:
  m=k*n-m
else:
  m=0
print(m)
