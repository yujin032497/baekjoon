# 2022-02-09
# 직각삼각형
while 1:
  N=list(map(int,input().split())) # 삼 변을 받는다.
  if sum(N)==0: break
  else:
    N=sorted(N) # 가장 긴 변이 리스트 끝에 오도록
    if N[0]**2+N[1]**2==N[2]**2: print('right') # 피타고라스 정의: a**2+b**2=c**2
    else: print('wrong')
