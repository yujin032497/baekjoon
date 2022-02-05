# 2022-02-05
# 수 정렬하기 3
import sys # 입력 메모리 줄이기 위해 sys.stdin.readline()을 사용
N=int(sys.stdin.readline())
M=[0]*10000 # 입력할 수 있는 수 범위까지 리스트 만들어서 개수 리스트
for _ in range(N):
    n=int(sys.stdin.readline())
    M[n-1]+=1
for i in range(0,len(M)): 
    if M[i]!=0: # 0이 아닌 것만
        for j in range(M[i]): 
            print(i+1) # i를 출력
