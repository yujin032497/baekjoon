#단어 공부
s=input()
a=[]
s1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
s=list(s.upper())
for i in s :
    a.append(ord(i))
for i in a :
    b=i-65
    s1[b]+=1
s2=list(filter(lambda x: s1[x]==max(s1),range(len(s1))))
if len(s2)>1:
    print("?")
else:
    print(chr(s2[0]+65))
