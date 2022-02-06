# 2022-02-06
# 수 정렬하기 4
import sys
M=[]
N=int(sys.stdin.readline())
for _ in range(N):
    M.append(int(sys.stdin.readline()))
for i in reversed(sorted(M)): # 오름차순 후 reversed를 통해 뒤집어서 내림차순으로
    print(i)
