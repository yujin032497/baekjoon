# 2022-01-09
# 주사위 세개
n=list(map(int, input().split()))
a=[0]*6 #주사위 위치 개수 저장
b=0
for i in n: # 주사위 위치 개수 세기
  a[i-1]+=1
for i in a:
  if i==3: # 위치 개수가 3이 있을 경우
    b=10000+(a.index(i)+1)*1000
  elif i==2: # 위치 개수가 2가 있을 경우
    b=1000+(a.index(i)+1)*100
if b==0: # 없을 경우
  b=list(filter(lambda x: a[x]==1, range(len(a)))) # 1인 경우만 리스트로 변환
  b=(max(b)+1)*100 # 그 중 가장 큰 수 
print(b)
