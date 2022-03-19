# 2022-03-19
# 약수
import sys
N=int(sys.stdin.readline()) # 몇 개의 정수를 입력받을지 입력
M=list(map(int,sys.stdin.readline().rstrip().split())) # 정수 입력
M.sort() # 오름차순으로 정렬
print(M[0]*M[-1]) # 약수는 제일 앞과 뒤를 곱하면 됨
