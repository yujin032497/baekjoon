# 2022-04-06
# 10부제
import sys
N=int(sys.stdin.readline()) # 10부제 실시하는 일의 자리 
M=list(map(int, sys.stdin.readline().rstrip().split())) # 차량 번호 일의 자리 5대
if N in M: print(M.count(N)) # 리스트안에 입력한 N 이 들어있다면 출력
else: print(0) # 리스트 안에 N 이 없으면 0 출력
