# 2021-01-04
# 화성 수학
n=int(input()) # 몇번 받을 것인지 입력
for i in range(0,n):
  a = list(input().split()) # 공백으로 입력을 구분하여 리스트에 넣기
  s=float(a[0]) # 리스트의 첫번째는 무조건 숫자이므로 실수로 변환
  for i in range(1,len(a)): # 리스트의 1번째부터 마지막번째까지 
    if a[i]=='@': # '@'이면 *3
      s*=3
    elif a[i]=='%': # '%'이면 +5
      s+=5
    elif a[i]=='#': # '#'이면 -7
      s-=7 
  print("%.2f" %s) # 소수점 둘째자리까지 실수 
