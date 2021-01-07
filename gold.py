import sys
input=sys.stdin.readline


# n=int(input())

# #n! , r! ,(n-r)!에서 2와 5의 제곱수를 구한다


# def twocount(a,n2_count=0):
#     i=2
#     while (a/i>=1):
#         n2_count+=a//i
#         i*=5
#     return n2_count

# def fivecount(a,n5_count=0):
#     i=5
#     while (a/i>=1):
#         # print(a)
#         n5_count+=a//i
#         i*=5
#     return n5_count

# a=1
# while True:
#     a=a*n
#     n-=1
#     if n==0:
#         break

# # print(a)
# # print()
# print(twocount(a))
# print(fivecount(a))
# last=min(twocount(a),fivecount(a))
# # print(last)
# # print(a%(10**last))


import sys
input=sys.stdin.readline
import heapq


t=int(input())
for _ in range(t):
    k=int(input())
    heap=[]

    for _ in range(k):
        a,n=map(str,input().rstrip().split())
        n=int(n)
        if a=='I':

            heapq.heappush(heap,(-n,n))

        else:
            if heap:
                if n==-1:
                    heapq.heappop(heap)[1]
                else:
                    heapq.heappop(heap)[0]
            else:
                continue
    print(heap)
    print(min(heap)[1])
    if heap:
        if len(heap)>=2:
            print(heapq.heappop(heap)[1],heapq.heappop(heap)[1])
        else:
            a=heapq.heappop(heap)[1]
            print(a,a)
    else:
        print('EMPTY')
