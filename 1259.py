# 2022-02-07
# 팰린드롬수
while 1:
    S=list(map(int,input()))
    if S[0]==0: break # 0을 입력하면 종료
    if S==list(reversed(S)): print('yes') # 리스트를 뒤집은거와 같은지 비교
    else: print('no')
