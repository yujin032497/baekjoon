# 2022-03-17
# 더하기 4
import sys
T=int(sys.stdin.readline().rstrip()) # 테스틑케이스 수
for _ in range(T):
  n=list(map(int,sys.stdin.readline().rstrip().split())) # 리스트에 숫자 입력
  print(f'{sum(n)}') # 리스트 합계
