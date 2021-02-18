import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
##Jsuyeon##
##유기농배추##
##알고리즘:dfs##
def dfs(graph,x,y,cnt,visited):
    if visited[x][y]==True:
        return cnt
    visited[x][y]=True
    cnt+=1

    if x+1<m:
        if visited[x+1][y]==False and graph[x+1][y]==1:
            dfs(graph,x+1,y,cnt,visited)            
    if x-1>-1:
        if visited[x-1][y]==False and graph[x-1][y]==1:
            dfs(graph,x-1,y,cnt,visited)
    if y+1<n:
        if visited[x][y+1]==False and graph[x][y+1]==1:
            dfs(graph,x,y+1,cnt,visited)
    if y-1>-1:
        if visited[x][y-1]==False and graph[x][y-1]==1:
            dfs(graph,x,y-1,cnt,visited)



t=int(input())
for _ in range(t):
    m,n,k=map(int,input().split())
    #가로길이,세로길이,배추 위치
    cabbage=[[0]*n for _ in range(m)]
    visited=[[False]*n for _ in range(m)]
    for _ in range(k):
        x,y=map(int,input().split())
        cabbage[x][y]=1

    cnt=0
    ans=0
    for i in range(m):
        for j in range(n):
            if cabbage[i][j]==1:
                a=((dfs(cabbage,i,j,cnt,visited)))
                if a == None:
                    ans+=1
            else:
                continue
    print(ans)

