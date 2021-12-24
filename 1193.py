#2021-12-24
#분수찾기
n=int(input())
m=i=j=1
w=0#아래:0, 위:1
while n>m:
    if n>m:
        i+=1
        m+=i
        if w==1:
            w=0
        else:
            w=1
    else:
        break;
if w==1:#위일경우
    for m in range(m,n,-1):
        if m!=n:
            i-=1
            j+=1
        else:  
            break
elif w==0:#
    j=i
    i=1
    for m in range(m,n,-1):
        if m!=n:
            i+=1
            j-=1
        else:
            break

print("%d/%d" %(i,j))
