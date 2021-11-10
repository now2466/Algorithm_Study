#16439백준 치킨치킨치킨

n, m = map(int, input().split())

global result, answer
result = []
for i in range(n):
    result.append(list(map(int, input().split())))

#print(result)

answer = 0
ch = [0] * m

def DFS(L, s):
    global answer
    if L == 3:
        sum = 0
        for i in range(n):
            sat = 0
            for j in range(m):
                if ch[j] == 1:
                    sat = max(sat, result[i][j])
            sum += sat
        answer = max(answer, sum)
    else:
        for i in range(s, m):
            if ch[i] == 0:
                ch[i] = 1
                DFS(L+1, i)
                ch[i] = 0

DFS(0,0)
print(answer)
