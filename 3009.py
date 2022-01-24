# 2022-01-24
# 네 번째 점
x,y=map(int,input().split()) # 처음 x,y 점을 받는다
for _ in range(2): # 나머지 두 점을 받는다
 x2,y2=map(int,input().split()) # 다른 x,y 점을 받아서
 x^=x2 # XOR 연산
 y^=y2
print(x,y)

# XOR 연산 특성 : A,B XOR을 한 후 다시 A를 XOR 하면 B
                                 다시 B를 XOR 하면 A
                                 
# 사각형의 점을 하기 위해서는 X,Y 각각 같은 자리 두번이 되야 한다.
