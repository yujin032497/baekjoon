# 2022-02-01
# 별 찍기 - 8
N=int(input())
for i in range(1,N+1):
    print('*'*i+' '*(2*N-i*2)+'*'*i)
for i in range(N-1,0,-1):
    print('*'*i+' '*(2*N-i*2)+'*'*i)
