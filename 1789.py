# 2022-01-09
# 수들의 합
n=int(input())
sum=0
for i in range(1,n+1):
  if sum+i<=n:
    sum+=i
  else:
    print(i-1)
    break
