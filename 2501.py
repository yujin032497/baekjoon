# 2022-02-04
# 약수 구하기
N,K=map(int,input().split()) #N: 자연수, K: 번째 약수
M=[] # 약수 리스트
for i in range(1,N+1):
    if N%i==0: # 나누어 떨어지면
        M.append(i) # 약수
if len(M)<K:print(0) # K가 리스트 요소 개수보다 크면 0
else:print(M[K-1]) # 아니면 K번째 출력
