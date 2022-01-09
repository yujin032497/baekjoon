# 2022-01-09
# 소인수분해
n=int(input())
for i in range(2,n+1,1): # 소수는 2부터 시작
  while True:
    if n%i==0:
      n//=i
      print(i)
    else:
      break
  if n==1: # 나누고 나눠서 1이면 반복문 
    break
