# 2022-01-30
# 직사각형에서 탈출
x,y,w,h=map(int,input().split()) # x,y,w,h

# 직선이 가장 가까운 위치이므로 (0,0),(x,y),(w,h)를 각각 뺀 것 중 가장 짧은 길이 출력
print(min(x-0,y-0,w-x,h-y)) 
