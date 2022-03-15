# 2022-03-15
# 괄호
import sys
T=int(sys.stdin.readline().rstrip()) # 테스트케이스 수
r='' # 결과값
for _ in range(0,T):
  b=0 
  S=list(sys.stdin.readline().rstrip()) # 괄호 입력
  while len(S)!=0:
    a=S.pop() # 리스트에서 하나씩 POP
    if a==')': b+=1 # ')'이면 b는 1증가
    else:
      b-=1 # '('이면 b는 1감소
      if b<0: break # 음수이면 '('부터 먼저 나온 것이므로 종료
  if b==0: r='YES' # 짝이 맞을 경우
  elif b!=0: r='NO' # 짝이 안맞거나 '('부터 나온 경우
  print(r)
