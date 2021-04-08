n=int(input())

i=1
s=1

if n==0:print(1)

else:
    while i<=n:
        s*=i
        i+=1
    print(s)
    
