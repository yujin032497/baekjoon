# 2022-02-01
# 별찍기 - 5
N=int(input()) # 찍을 별 줄 수
for i in range(1,N+1):
    print(' '*(N-i)+'*'*(2*i-1),end='\n') # 양 옆의 빈칸이 아닌 왼쪽만 빈칸하고 줄바꿈
