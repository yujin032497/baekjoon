# 2022-02-08
# 나이순 정렬
import sys
M=[] # 나이, 이름 리스트
N=int(sys.stdin.readline().rstrip()) # N 명수
for _ in range(N):
    a,b=sys.stdin.readline().rstrip().split() # a: 나이, b: 이름
    M.append([int(a),b])
M.sort(key=lambda x: x[0]) # 나이 순으로 오름차순
for i in M:
    print(i[0], i[1])
