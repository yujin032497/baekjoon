#2021-12-25
#달팽이는 올라가고 싶다
a,b,v=map(int, input().split())
c=(v-a)//(a-b)+1
if (v-a)%(a-b)!=0:
  c+=1
print(c)
