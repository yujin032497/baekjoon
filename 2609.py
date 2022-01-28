# 20022-01-28
# 최대공약수와 최소공배수
t=[0]*3
t2=1
n,m=map(int,input().split())
a=n
b=m
while 1:
  r=a%b # 유클리드 호제법: (a,b)=(b,r)
  a=b
  b=r
  if r==0: break # 나머지가 0인 경우 반복종료
n//=a
m//=a
print(a) # 최대공약수
print(n*m*a) # 최소공배수
