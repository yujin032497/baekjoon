# 2022-01-14
# 그릇
s=input()
t=10
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        t+=5
    else:
        t+=10
print(t)
