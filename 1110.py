#더하기 사이클
s1=input()
if int(s1)<10:
    s1='0'+s1
s2=s1
i=0
while True:
    i+=1
    if (int(s1[0])+int(s1[1]))<10:
        num=s1[1]+str(int(s1[0])+int(s1[1]))

    else:
        num=s1[1]+str((int(s1[0])+int(s1[1]))%10)
    if s2==num:
        break;
    s1=num
print(i)
