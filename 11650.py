# 2022-02-08
# 좌표 정렬하기
import sys
M=[]
N=int(sys.stdin.readline().rstrip()) # N개 좌표
for _ in range(N):
    x,y=map(int,sys.stdin.readline().rstrip().split()) # x,y좌표
    M.append([x,y])
M.sort(key=lambda x: (x[0], x[1])) # 오름차순 순위: x좌표, y좌표 순서로
for i in M:
    print(i[0], i[1])
