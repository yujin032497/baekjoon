# 2022-01-19
# 사분면
n=int(input())
q=[0]*5
for i in range(0,n):
  n,m=map(int,input().split())
  if n==0 or m==0: #축
    q[4]+=1
  elif n>0 and m>0: # 제1사분면
    q[0]+=1
  elif n<0 and m>0: # 제2사분면
    q[1]+=1
  elif n<0 and m<0: # 제3사분면
    q[2]+=1
  elif n>0 and m<0: # 제4
    q[3]+=1
for i in range(len(q)-1):
  print("Q%d: %d" %(i+1, q[i]))
print("AXIS: %d" %(q[4]))
