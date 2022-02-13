# 2022-02-13
# 좌표 정렬하기 2
import sys
T=[] # 좌표 리스트
N=int(sys.stdin.readline().rstrip()) # 입력할 좌표 개수
for _ in range(N):
  x,y=map(int,sys.stdin.readline().rstrip().split()) # x,y 좌표 입력
  T.append([x,y])
T.sort(key=lambda x:(x[1],x[0])) # 오름차순 순서: 1.y좌표 2.x좌표
for i in T:
  print(i[0],i[1])
