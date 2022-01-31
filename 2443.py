# 2022-02-01
# 별 찍기 - 6
N=int(input()) # 찍을 별 줄 수
for i in range(N,0,-1):
    print(' '*(N-i)+'*'*(2*i-1))
