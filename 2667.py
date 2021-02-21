import sys
input=sys.stdin.readline


n=int(input())
dangi=[]
for _ in range(n):
    temp=[]
    for val in input().rstrip():
        temp.append(int(val))
    dangi.append(temp)



def dfs(graph,i,j,visited):
    global cnt
    if visited[i][j]==True:
        return cnt
    visited[i][j]=True
    graph[i][j]=0
    cnt+=1

    if i+1<n:
        if visited[i+1][j]==False and graph[i+1][j]==1:
            dfs(graph,i+1,j,visited)
    if i-1>-1:
        if visited[i-1][j]==False and graph[i-1][j]==1:
            dfs(graph,i-1,j,visited)
    if j+1<n:
        if visited[i][j+1]==False and graph[i][j+1]==1:
            dfs(graph,i,j+1,visited)
    if j-1>-1:
        if visited[i][j-1]==False and graph[i][j-1]==1:
            dfs(graph,i,j-1,visited)
    
    return cnt

visited=[[False]*n for _ in range(n)]

a=[]

for i in range(n):
    for j in range(n):
        if dangi[i][j]==0:
            continue
        cnt=0
        ans=dfs(dangi,i,j,visited)
        if ans==None:
            pass
        else:
            a.append(ans)
print(len(a))
a.sort()
for i in a:
    print(i)


