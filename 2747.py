# 2022-01-27
# 피보나치 수
n=int(input()) #n번째까지 
s=[0,1]+[0]*(n-1) # 1번째, 두번째는 0,1 나머지는 0배열로 채운다 
                  # 0은 n번째에 포함하지 않는다
for i in range(2,n+1): #
  s[i]=s[i-2]+s[i-1] # n = n-1 + n-2
print(s[n]) # n번째 수 출력
