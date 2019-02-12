st1,st2,k=raw_input().split()
c1=0
c2=0
for x in st1:
	if x not in st2:
		c1=c1+1
for x in st2:
	if x not in st1:
		c2=c2+1
if(c1==c2==int(k)):
	print("yes")
else:
	print("no")
