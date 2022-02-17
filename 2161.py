# 2022-02-17
# 카드 1
import sys
M=[]
N=int(sys.stdin.readline()) # 카드 N장
C=[x for x in range(1,N+1)] # 1 ~ N까지의 카드 리스트
while len(C)>1: # 1장 남을때까지
    print(C[0]) # 버리는 카드
    del C[0] # 버리고
    C.append(C[0]) # 넘기고
    del C[0] # 넘긴카드 버리기
print(C[0]) # 마지막 남은 카드 = 마지막에 버리는 
