#2021-12-28
#부녀회장이 될테야
def s(m):
    for i in range(len(a)):
        if i==0:
            continue
        else:
           a[i]=sum(a[i-1:i+1])
    return a
t=int(input())#테스트개수
k=[]#층
n=[]#호실
i=j=0
for i in range(0,t):#테스트개수만큼 입력을 리스트에 저장
    k.append(int(input()))
    n.append(int(input()))
i=0
while i<t:
    l=0
    a=list(range(1,n[i]+1))#리스트1~n까지 초기화
    while l<k[i]:#층수까지 반복
        a=s(a)
        l+=1
    i+=1
    print(a[-1])#리스트 마지막 인덱스:n호실




