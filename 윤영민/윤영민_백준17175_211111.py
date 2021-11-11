import sys
n = int(sys.stdin.readline())

dy = [0]*51
dy[0]=1
dy[1]=1
for i in range(2,51):
    dy[i]=dy[i-1]+dy[i-2]+1

print(dy[n]%1000007)
