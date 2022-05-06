# 2022-05-06
# 단어 뒤집기
import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    result=[] # 결과값
    s = list(sys.stdin.readline().rstrip().split()) # 문자열입력
    for t in s:
        result.append(t[::-1]) # 문자열 뒤집기 [::-1]:reverse
    print(' '.join(result)) #.join을 통해 리스트->
