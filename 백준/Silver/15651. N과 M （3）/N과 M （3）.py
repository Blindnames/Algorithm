import sys
input = sys.stdin.readline


def dfs(l):
    if l == m:
        for i in range(m):
            print(res[i], end=" ")

    else:
        for i in range(1, n+1):
            res[l] = i
            dfs(l+1)


n, m = map(int, input().split())
res = [0]*m
dfs(0)
