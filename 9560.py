# 2022-01-20
# 약수들의 합
import math 
k=[] # k: 입력한 n의 약수집합
while 1:
  n=int(input())
  if n==-1: # -1을 입력하면 입력종료
    break
  for i in range(1,int(math.sqrt(n))+1): # 입력한 수의 제곱근까지
    if i in k: # 약수 집합 list에 i가 존재하면
      break # 반복종료
    if n%i==0: # 입력한 수를 i로 나누어떨어지면
      k.append(i) # 약수 집합에 넣음
      if n//i!=n: # 약수 중 자기 자신이 아니면
       k.append(n//i) # 약수 집합에 몫을 넣음
  k.sort() # 약수들을 오름차순으로 정렬
  s=str(n)+" = " 
  for i in range(len(k)):
    s+=str(k[i])+" + "
  if sum(k)==n: # 약수들의 집합의 합 = 입력한 수
    print(s[:-2]) # 마지막 문자 '+'를 제외하기 위함
  else: # 약수들의 집합의 합 != 입력한 수
    print("%d is NOT perfect." %(n))
  k=[]
