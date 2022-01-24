# 2022-01-25
# 완전제곱수
import math
k=[]
n=int(input()) # 첫 번째 수 입력
m=int(input()) # 두 번째 수 입력
for i in range(int(math.sqrt(m))+1): # 두 번째 수의 제곱근까지 반복 
  if i**2>=n: # i의 제곱이 n보다 크면
    k.append(i**2) 
if len(k)==0: # 리스트에 아무것도 없으면 -1
  print(-1)
else: # 리스트 합, 완전제곱 중 가장 작은 수 
  print(sum(k))
  print(k[0])
