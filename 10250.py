#2021-12-26
#ACM호텔
n=int(input())
arr=[list(map(int, input().split())) for _ in range(n)]
h=w=m=a=b=0
for i in range(0,n):
  h=arr[i][0] #호텔높이
  w=arr[i][1] #호텔넓이
  m=arr[i][2] #n번째 사람
  if m%h==0:
      b=h
      a=m//h
  else:
      b=m%h
      a=m//h+1
  print(b*100+a)
