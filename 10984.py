T=int(input()) # 학기의 수
for _ in range(0,T):
    C=G=0 # C: 학점의 합 G: 성적의 합
    N=int(input()) # 과목 수
    for _ in range(0,N):
        c,g=map(float,input().split()) # c: 학점, g: 성적
        C+=int(c)
        G+=int(c)*g
    print("%d %.1f" %(C, G/C))    
