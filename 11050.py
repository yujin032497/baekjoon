# 2022-02-16
# 이항 계수 1
def f (a): #팩토리얼함수
  b=1
  for i in range(1,a+1):
    b*=i
  return b
N,K=map(int,input().split()) # N,K
print(f(N)//(f(K)*f(N-K)))
