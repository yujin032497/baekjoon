#2021-01-03
#인공지능 시계
a,b,c=map(int, input().split())
d=int(input())
t=a*60*60+b*60+c+d
b,c=divmod(t,60)#divmod(나누어지는수, 나누려는 수) 몫과 나머지를 각각 도출
a,b=divmod(b,60)
a%=24
print("%d %d %d" %(a,b,c))
