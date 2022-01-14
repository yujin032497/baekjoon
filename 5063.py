# 2022-01-14
# TGN
n=int(input())
for i in range(0,n):
    r,e,c=map(int,input().split()) # r = 광고를 하지 않을 때 수익, e = 광고를 했을 때 수익, c = 광고비용
    if r<e-c: # 광고를 하지 않을 때 수익 < 광고를 했을 때 수익 - 광고비용
        s="advertise"
    elif r==e-c: # 광고를 하지 않을 때 수익 == 광고를 했을 때 수익 - 광고비용
        s="does not matter"
    else: # 광고를 하지 않을 때 수익 > 광고를 했을 때 수익 - 광고비용
        s="do not advertise"
    print(s)
