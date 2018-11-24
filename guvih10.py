a,b=raw_input().split()
c=raw_input().split()
d=raw_input().split()
a=int(a)
b=int(b)
e=len(d)
flag=0
if(len(c)==a and len(d)==b):
	for j in d:
		if j in c:
			flag=flag+1
	if(flag==e):
		print "YES"
	else:
		print "NO"
else:
	print "invalid"
