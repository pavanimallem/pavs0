N,K=map(int,raw_input().split())
c=list(str(N))
e=K
while e>0:
    e=e-1
    del(c[e])
print(''.join(c))
