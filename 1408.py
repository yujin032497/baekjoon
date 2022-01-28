# 2022-01-28
# 24
h1,m1,s1=map(int,input().split(':')) # 현재 시각 입력
h2,m2,s2=map(int,input().split(':')) # 임무 시각 입력
t1=h1*3600+m1*60+s1 # 초로 환산
t2=h2*3600+m2*60+s2
if t2>t1: # 현재 시각 < 임무 시각
  i=t2-t1
else:
  i=86400-t1+t2 # 임무 시각 < 현재 시각
s=i%60 # 초로 환산
m=i//60%60 #분으로 환산
h=i//3600 # 시로 환산
print("%s:%s:%s" %(format(h,'02'),format(m,'02'),format(s,'02'))) # 00:00:00 으로 변환 # format()을 사용하면 str 로 결과
