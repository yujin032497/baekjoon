#그룹 단어 체커
def cal(t):
    for k in range(len(t)):
        if k+1==len(t):
            return 1
        else:
            if t[k]+1!=t[k+1]:
                return -1

t=[]
m=0
n=int(input())
s=list(input() for _ in range(n))
for i in range(len(s)):
    m+=1
    s2=list(set(s[i]))
    for j in s2:
      t=list(filter(lambda x: s[i][x]==j, range(len(s[i]))))
      if len(t)!=1:
          if cal(t)==-1:
              m-=1
              break
         
print(m)


