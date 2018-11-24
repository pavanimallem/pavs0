n=int(raw_input())
a=[int(x) for x in raw_input().split()]
a.sort()
i=0;j=n-1
min=9999
while i<j:
    if min>abs(a[i]+a[j]):
        min=abs(a[i]+a[j])
        x=a[i]
        y=a[j]
    if a[i]+a[j]<0:
        i+=1
    else:
        j-=1
    
print x,y
