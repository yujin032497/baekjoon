# 2022-01-30
# 체스판 다시 칠하기
c=[] # 체스판 리스트
t=[] # 다시 칠한 횟수 리스트
N,M=map(int,input().split()) # 가로, 세로
for _ in range(N): # 가로만큼 세로줄 입력
    c.append(input())
for a in range(N-7): # 8*8 이므로 입력한 가로, 세로만큼 -7 (첫줄은 이미 시작하기 때문)
    for b in range(M-7):
        x=0 # 흰색이 첫칸일때
        y=0 # 검은색이 첫칸일떄
        for i in range(a,a+8): # 처음시작점의 +8만큼 탐색 (8*8이기 떄문)
            for j in range(b,b+8):
                if (i+j)%2==0: # (0,0)부터 시작이 짝수
                    if c[i][j]!='W': # 첫 칸부터 흰색이 아니면
                        x+=1 # 검은색으로 다시 칠하기
                    if c[i][j]!='B': # 첫 칸부터 검은색이 아니면
                        y+=1 # 흰색으로 다시 칠하기
                else:
                    if c[i][j]!='B':
                        x+=1
                    if c[i][j]!='W':
                        y+=1
        t.append(x)
        t.append(y)
print(min(t)) # 최소 횟수 출력
