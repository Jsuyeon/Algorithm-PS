import sys
input=sys.stdin.readline
import heapq
# from collections import deque
###Jsuyeon###

t=int(input())
for _ in range(t):
    k=int(input())
    visitied=[False]*1000001
    heap_max=[]
    heap_min=[]
    # heap=[]
    for i in range(k):
        a,n=map(str,input().rstrip().split())
        n=int(n)
        if a=='I':
            heapq.heappush(heap_max,(-n,i))
            heapq.heappush(heap_min,(n,i))
            visitied[i]=True
            #값이 들어갔다
        else:
            if n==-1:
                #최솟값을 삭제
                while heap_min and not visitied[heap_min[0][1]]:
                    heapq.heappop(heap_max)  
                if heap_min:
                    visitied[heap_min[0][1]]=False
                    heapq.heappop(heap_min)                      

                print(heap_max)
                print(heap_min)
            elif n==1:
                #최댓값을 삭제
                while heap_max and not visitied[heap_max[0][1]]:
                    heapq.heappop(heap_min)
                if heap_max:
                    visitied[heap_max[0][1]]=False
                    heapq.heappop(heap_max)

                print(heap_max)
                print(heap_min)
        # print(heap)
    while heap_max and not visitied[heap_max[0][1]]:
        heapq.heappop(heap_max)
    while heap_min and not visitied[heap_min[0][1]]:
        heapq.heappop(heap_min)
    if heap_max and heap_min:
        print(f'{-heap_max[0][0]} {heap_min[0][0]}')
    else:
        print('EMPTY')
