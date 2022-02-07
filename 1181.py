# 2022-02-07
# 단어 정렬
import sys
N=int(sys.stdin.readline())
S=[]
for i in range(N):
    S.append(sys.stdin.readline().rstrip())
S=sorted(list(set(S))) # 중복제거 후 오름차순 정렬
S.sort(key=lambda x: len(x)) # 길이 정렬
for i in S:
    print(i)
