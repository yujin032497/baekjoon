# 2022-01-21
# Yangjojang of The Year
from sys import stdin # stdin.readline()을 통해 시간 단축
t=int(stdin.readline()) # 테스트 케이스 수
u=[] # u: 대학교 이름
s=[] # s: 소주 병 수
for _ in range(t):
  n=int(stdin.readline()) # n: 학교 수
  for _ in range(n):
    a,b=stdin.readline().split()
    u.append(a)
    s.append(int(b)) # 소주 병 수는 int()형으로 변환해서 넣음
  print(u[s.index(max(s))]) # 소주 병 수가 가장 많은 index를 구해 대학교 반환
