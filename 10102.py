# 2022-01-15
# 개표
n=int(input())
s=input()
a=b=0 # a: A 투표 개수, b: B투표 개수 
for i in range(0,n):
 if s[i]=='A':
    a+=1
 else:
    b+=1
if a>b: # A 투표 개수가 많으면
  print('A')
elif b>a: # B 투표 개수가 많으면
  print('B')
else: # A,B 투표 개수가 
  print("Tie")
