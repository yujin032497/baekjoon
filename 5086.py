# 2022-01-17
# 배수와 약수
while 1: # 무한반복
  a,b = map(int, input().split()) # 두 수를 받는다
  if a==0 and b==0: # 두 수가 모두 0이면 종료
    break;
  else:
    if a<b and b%a==0: # 약수일 경우
      s="factor"
    elif b<a and a%b==0: # 배수일 경우
      s="multiple"
    else: # 약수, 배수 둘 다 
      s="neither"
    print(s)
