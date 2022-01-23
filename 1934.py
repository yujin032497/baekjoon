# 2022-01-23
# 최소공배수
# 유클리드 호제법 사용
n=int(input()) # 테스트 케이스 몇 개 입력할지
for _ in range(n):
  r=1 # 나머지
  a,b=map(int,input().split()) # 두 수 입력
  i=a
  j=b
  while r!=0: # 나머지가 0이 아닐 때까지
    r=i%j
    i=j
    j=r
  print(a*b//i) 
