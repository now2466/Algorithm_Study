n,k = map(int,input().split())

block_list = list(map(int,input().split()))


answer=n

for i in range(n):
    count = 0
    for j in range(n):
        if block_list[j]!=block_list[i]+((j-i)*k):
            count+=1
        if block_list[i]+((j-i)*k)<1:
            count=n
            break
    answer=min(answer,count)

print(answer)
