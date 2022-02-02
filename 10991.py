# 2022-02-02
# 별 찍기 - 16
N=int(input()) # 찍을 별 줄 수
for i in range(0,N):
    s=''
    for j in range(1,2*N):
        if j>=(N-i) and j<=(N+i):
            if N%2==0: # 찍을 별 줄 수 가 짝수 일 때,
                if i%2==0 and j%2==0: # 행,열이 짝수인 경우
                    s+='*'
                elif i%2!=0 and j%2!=0: # 행,열이 홀수인 경우
                    s+='*'
                else:
                    s+=' '
            else: # 찍을 별 줄 수 가 홀수 일 때,
                if i%2==0 and j%2!=0: # 행이 짝수이고 열이 홀수 일 때
                    s+='*'
                elif i%2!=0 and j%2==0: #행이 홀수이고 열이 짝수 일 때
                    s+='*'
                else:
                    s+=' '
        else:
            s+=' '
    print(s.rstrip())
    
    
N=int(input())
for i in range(1,N+1):
    print(' '*(N-i)+'*'*i)
