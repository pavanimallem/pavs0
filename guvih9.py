n=int(raw_input())
m=[int(x) for x in raw_input().split()]
m.sort
for i in range(0,n):
    for j in range(i+1,n):
        if(m[i]+m[j]==0):
            print m[i],m[j]
    else:
       print 0
