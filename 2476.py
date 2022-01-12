# 2022-01-12
# 주사위 게임
n=int(input()) #사람 수
a=b=c=0
for i in range(0,n):
  m=list(map(int,input().split()))
  b=0
  for j in range(0,len(m)):
    a=m.count(m[j])
    if a==3: # 주사위 던진 수가 중 중복 3개일 떄
      b=10000+m[j]*1000
      break
    elif a==2: # 주사위 던진 수가 중 중복 2개일 떄
      b=1000+m[j]*100
      break
  if b==0: # 주사위 던진 수가 중 중복X
    b=max(m)*100
  if c<b: # 던진 주사위 합산 중 큰 사람 
    c=b
print(c)
