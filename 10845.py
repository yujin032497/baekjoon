import sys
Q=[] # 큐 리스트
N=int(sys.stdin.readline().rstrip()) # 명령어 개수
for _ in range(N):
  s=sys.stdin.readline().rstrip().split() # s[0]: 명령어 s[1]: 정수
  if s[0]=='push':Q.insert(0,s[1]) # 0번째에 삽입
  elif s[0]=='pop':
    if not Q:n=-1 # Q에 요소가 없으면 -1
    else:n=Q.pop() # Q의 맨 뒤 요소 제거
  elif s[0]=='size':n=len(Q) # Q 리스트 요소 개수
  elif s[0]=='empty':
    if not Q: n=1 # Q 리스트가 비어있으면
    else: n=0 # Q 리스트가 비어있지않으면
  elif s[0]=='front':
    if not Q:n=-1 # Q 리스트에 요소가 없으면 -1
    else:n=Q[-1] # Q 리스트의 맨 뒤 요소
  elif s[0]=='back': 
    if not Q:n=-1 # Q 리스트에 요소가 없으면 -1
    else:n=Q[0] # Q 리스트의 맨 앞 요소
  if s[0]!='push':print(n) # push를 제외한 나머지 명령어의 영향받은 정수 출력
    
# 큐: 리스트 맨 앞: back
#     리스트 맨 뒤: front
