# 2021-01-07
# 평균 점수
p=[int(input()) for x in range(0,5)]
for i in range(len(p)):
  if p[i]<40:
    p[i]=40
print(sum(p)//len(p))
