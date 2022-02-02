# 2022-02-02
# 별 찍기 - 15
N=int(input()) # 찍을 별 줄 수
for i in range(0,N):
    s=''
    for j in range(1,2*N):
        if j==(N-i) or j==(N+i):
            s+='*'
        else:
            s+=' '
    print(s.rstrip())
#    *     i=0 j=3        
#   * *    i=1 j=2, j=4   N-i, N+i
#  *   *   i=2 j=1, j=5   
