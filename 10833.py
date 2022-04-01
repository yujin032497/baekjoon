# 2022-04-01
# 사과
import sys
sum=0 # 남은 사과 합계
A=int(sys.stdin.readline()) # 학교 수
for _ in range(0,A):
    N,M=map(int,sys.stdin.readline().rstrip().split()) # N : 학교의 학생 수, M : 배정된 사과의 수
    sum+=(M%N) # 배정된 사과의 수 / 학교의 학생 수의 나머지
print(sum) # 남은 사과의 합계
