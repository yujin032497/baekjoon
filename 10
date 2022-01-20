# 2022-01-20
# Baseball
from sys import stdin # 시간을 단축시키기 위해 stdin.readline()으로 씀
n=int(stdin.readline()) n: 테스트 케이스 수
for _ in range(0,n):
  Y=K=0 # Y: 연세대 총 점수 K: 고려대 총 점수
  for _ in range(9):
     y,k=map(int,stdin.readline().split()) # y: 연세대가 획득한 점수 k: 고려대가 획득한 점수
     Y+=y: # 획득한 점수만큼 더함
     K+=k
  if Y>K:s='Yonsei' # 연세대 총 점수 > 고려대 총 점수
  elif K>Y:s='Korea' # 고려대 총 점수 > 연세대 총 점수
  else:s='Draw' # 연세대 총 점수 = 고려대 
  print(s)
