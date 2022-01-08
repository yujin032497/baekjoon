# 2022-01-09
# 크냐?
while 1: #무한반복
  a,b=map(int,input().split())
  if a==0 and b==0: # 0 0일경우 종료
    break
  elif a>b:
    print("Yes")
  else:
    print("No")
