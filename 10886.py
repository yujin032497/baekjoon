# 2021-01-07
# 0 = not cute / 1 = cute
n=int(input())
m=[int(input()) for x in range(0,n)]
if m.count(1)>m.count(0):
  print("Junhee is cute!")
else:
  print("Junhee is not cute!")
