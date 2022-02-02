# 2022-02-03
# 별 찍기 - 20
N=int(input()) # 찍을 별 줄 수
for i in range(1,N+1):
    if i%2!=0: print('* '*(N-1)+'*') # i가 홀 수일때
    else: print(' *'*N) # i가 짝 수일때
