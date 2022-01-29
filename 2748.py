# 2022-01-29
# 피보나치 수 - 2
n=int(input()) # n 번째 피보나치 수 
f=[0,1]+[0]*(n-1) # 피보나치 수 리스트
for i in range(2,n+1):
  f[i]=f[i-1]+f[i-2] # (n-1)+(n-2)
print(f[n])
