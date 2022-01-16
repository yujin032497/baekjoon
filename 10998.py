# 2022-01-16
# 팰린드롬인지 확인하기
s=input() # 문자열을 받는다
t=s[::-1] # slice를 통해 역순
if s==t:
  a=1
else:
  a=0
print(a)
