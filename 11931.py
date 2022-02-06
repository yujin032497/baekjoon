# 2022-02-06
# 수 정렬하기 4
import sys
M=[]
N=int(sys.stdin.readline())
for _ in range(N):
    M.append(int(sys.stdin.readline()))
for i in reversed(sorted(M)):
    print(i)
