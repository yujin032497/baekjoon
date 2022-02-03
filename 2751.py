# 2022-02-04
# 수 정렬하기 2
import sys
N=int(sys.stdin.readline())
M=[]
for _ in range(N):
    M.append(int(sys.stdin.readline()))
M.sort() # 1440ms,75692KB M=sorted(M) : 1560ms 83508KB
for i in M:
    print(i)
