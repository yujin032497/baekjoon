# 2022-02-08
# 블랙잭
import sys
r=0
N,M=map(int,sys.stdin.readline().rstrip().split()) # N: 카드 수, M: 최대값
C=[int(x) for x in sys.stdin.readline().rstrip().split()] # 카드 리스트
for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            s=C[i]+C[j]+C[k]
            if s>r and s<=M:
                r=s
print(r)
