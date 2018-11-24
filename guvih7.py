n=int(raw_input())
l=[int(x) for x in raw_input().split()]
min=-1
m=[]
for i in range(0,n):
	for j in range(i+1,n):
		if l[i]==l[j]:
			min=i
			m.append(l[j])
if min!=-1:
	print m[0]
else:
	print "unique"
