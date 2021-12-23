#평균
n=int(input())
score=list(map(int,input().split()))
max=max(score)
new_score=0
for i in range(len(score)):
    new_score+=(score[i]/max*100)
print(new_score/n)
