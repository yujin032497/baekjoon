# 2022-02-19
# 덱
import sys
D=[]
N=int(sys.stdin.readline().rstrip())
for _ in range(N):
    S=sys.stdin.readline().rstrip().split()
    if S[0]=='push_front': D.insert(0,S[1])
    elif S[0]=='push_back': D.append(S[1])
    elif S[0]=='pop_front':
        if not D: n=-1
        else:
            n=D[0] 
            D.remove(D[0])
    elif S[0]=='pop_back':
        if not D: n=-1
        else: n=D.pop()
    elif S[0]=='size': n=len(D)
    elif S[0]=='empty':
        if not D: n=1
        else: n=0
    elif S[0]=='front':
        if not D: n=-1
        else: n=D[0] 
    elif S[0]=='back':
        if not D: n=-1
        else: n=D[-1]
    if S[0]!='push_front' and S[0]!='push_back':
        print(n)
    
    
