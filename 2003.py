# 2022-03-15
# 수들의 합2
import sys
N,M=map(int,sys.stdin.readline().rstrip().split()) # N개의 수 M
A=list(map(int,sys.stdin.readline().rstrip().split())) # N만큼 수 입력
left=0
right=0
sum=A[0]
cnt=0
# 투 포인트 알고리즘 활용
while 1:
  if sum<M:
    right+=1
    if len(A)-1<right:break # right가 len(A)-1보다 작으면 종료(index는 A길이 -1)
    sum+=A[right]
  elif sum==M:
    cnt+=1
    sum-=A[left]
    left+=1
  elif sum>M:
    sum-=A[left]
    left+=1
print(cnt)
