# 2022-02-03
# 수 찾기
N=int(input())
A=set([X for X in input().split()]) # B 리스트에 A가 있는지 없는지 확인하므로 중복 제거
M=int(input())
B=[X for X in input().split()]
for i in range(0,len(B)):
    if B[i] in A:print(1)
    else:print(0)
