# 2022-02-01
# 얼마?
T=int(input()) # 테스트 케이스 수
for _ in range(T):
    t=0 # 옵션 가격
    s=int(input()) # 자동차 가격
    n=int(input()) # 옵션 개수
    for _ in range(n):
        q,p=map(int,input().split()) # q : 각 옵션 개수, p : 옵션 개
        t+=q*p
    print(s+t)
