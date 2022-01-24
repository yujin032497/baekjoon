# 2022-01-25
# 첼시를 도와줘!
n=int(input()) # 테스트 케이스 수
for _ in range(n): 선수의 수
  m=int(input())
  c=[] # 가격
  d=[] # 선수 이름
  for _ in range(m):
    a,b=input().split()
    c.append(b)
    d.append(int(a))
  print(c[d.index(max(d))]) # 가격 중 가장 비싼 수의 index를 선수 이름 리스트의 index로 
