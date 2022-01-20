# 2022-01-20
# 주사위 게임
c=s=100 # c: 창영점수 s: 상덕점수
for i in range(int(input())): # 입력한 수 만큼 게임한다.
  a,b=map(int,input().split()) # a: 창영이가 던진 주사위 눈 b: 상덕이가 던진 주사위 눈
  if a<b:c-=b # 창영이의 주사위 눈이 작으면 창영이의 점수 -1 감소
  elif b<a:s-=a # 상덕이의 주사위 눈이 작으면 상덕이의 점수 -1 감소
print(c)
print(s)
