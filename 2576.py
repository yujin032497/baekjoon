# 2022-02-10
# 홀수
N=[] # 자연수
M=[] # 홀수
for _ in range(7): 
  N.append(int(input())) # 7개의 자연수를 받는다
for i in N:
  if i%2!=0: # 홀수인경우 M 리스트에 삽입
    M.append(i)
if len(M)==0: print(-1) # M 리스트에 요소 개수가 0
else:
  print(sum(M)) # 홀수들의 합
  print(min(M)) # 최소 홀수
