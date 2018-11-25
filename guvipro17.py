n,m=(int,raw_input().split())
l=[int(x) for x in raw_input().split()]
n=len(l)
for i in range(0,n-1):
	for j in range(i+1,n):
		if m==l[i]+l[j]:
			print("yes")
else:
	print("no")
