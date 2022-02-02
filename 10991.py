# 2022-02-02
# 별 찍기 - 16
N=int(input())
for i in range(0,N):
    s=''
    for j in range(1,2*N):
        if j>=(N-i) and j<=(N+i):
            if N%2==0:
                if i%2==0 and j%2==0:
                    s+='*'
                elif i%2!=0 and j%2!=0:
                    s+='*'
                else:
                    s+=' '
            else:
                if i%2==0 and j%2!=0:
                    s+='*'
                elif i%2!=0 and j%2==0:
                    s+='*'
                else:
                    s+=' '
        else:
            s+=' '
    print(s.rstrip())
    
    
N=int(input())
for i in range(1,N+1):
    print(' '*(N-i)+'*'*i)
