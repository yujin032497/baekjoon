# 2022-03-15 
# 수들의 합 5
import sys
N=int(sys.stdin.readline().rstrip()) # N까지의 수 입력
sum=1 # 구간 합계
left=1
right=1
cnt=0 #수열들의 합이 N과 같은 개수
# 투 포인터 알고리즘 활용
while left<=right: 
  if sum<N: # 합계가 N보다 작으면
    right+=1 # 오른쪽 1증가
    sum+=right
  elif sum==N: # 합계가 N가 같으면
    cnt+=1 # 개수 증가
    sum-=left # 현재 왼쪽만큼 빼고
    left+=1 # 왼쪽 1증가
  elif sum>N: # 합계가 N보다 크다면
    sum-=left # 현재 왼쪽만큼 빼고
    left+=1 # 왼쪽 1증가
print(cnt)
