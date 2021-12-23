#2021-12-23
#벌집
n=int(input())
m=o=1
while 1:
    if n>m:
        m=m+(6*o)
        o+=1
    else:
        break
print(o)
