import sys
input = sys.stdin. readline

c,k=map(int, input().split())

a=str(c)

if k ==0:
    print(c)
    sys.exit()
if len(a) < k:
    print(0)
    sys.exit()
if int(a[-k]) >= 5 :
    print(((c//(10**k))+1)*(10**k))
else:
    print((c//(10**k))*(10**k))