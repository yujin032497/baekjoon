# 2022-01-25
# 생일
m=int(input()) # 사람 명 수
a={} # key: 이름, value: 생일 
for i in range(m):
  n,d,m,y=input().split() # n: 사람이름, d: 일, m: 월, y: 년
  d=d.zfill(2) # 일,월 '00'으로 맞춤
  m=m.zfill(2)
  a[n]=y+m+d # 년월일을 문자열로 ex)19911001
print(max(a,key=a.get)) # a 딕셔너리에서 max의 key 값 (a.get을 통해 value의 최대값 키 반환)
print(min(a,key=a.get)) # a 딕셔너리에서 min의 key 값
