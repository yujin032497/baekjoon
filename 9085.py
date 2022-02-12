# 2022-02-12
# 더하기
T=int(input()) # 테스트 케이스 수
for _ in range(T):
  N=int(input()) # 입력할 수 갯수
  n=list(map(int,input().split()))
  print(sum(n)) # 합계
