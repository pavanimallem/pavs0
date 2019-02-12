l,r=map(int,raw_input().split())
count=0
for x in range(l+1,r):
	for y in range(1,r):
		temp=y*y
		if temp==x:
			count+=1
print count
