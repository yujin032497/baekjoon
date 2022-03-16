# 2022-03-26
# 수 이어쓰기 3
import sys
N=int(sys.stdin.readline().rstrip()) # N만큼 이어쓸 숫자
s=''
for i in range(1,N+1):
  s+=str(i) # N까지 숫자 이어 붙이기
print(s.find(str(N))+1) # find()함수로 N위치 찾기
