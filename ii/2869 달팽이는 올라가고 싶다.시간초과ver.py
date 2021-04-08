a,b,v=map(int,input().split())

s=0
day=1

while s<v:
    s+=a
    if s>=v: break
    s-=b
    day+=1

print(day)
