# 2022-03-19
# 더하기 2
s = ''
while 1:
    try:
        s+=input() # input()은 더 이상 입력이 없으면 EOFError() 반환, 
                   # sys.stdin.readline()은 입력이 없으면 빈 문자열 반환
    except:
        break
print(sum(map(int, s.split(','))))
