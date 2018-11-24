a,b=raw_input().split()
c=raw_input().split()
d=raw_input().split()
a=int(a)
b=int(b)
e=len(d)
count=0
if(len(c)==a and len(d)==b):
	for i in d:
		if i in c:
			count=count+1
	if(count==e):
		print "YES"
	else:
		print "NO"
else:
	print "invalid"
