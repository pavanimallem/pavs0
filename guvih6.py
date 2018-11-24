n=int(raw_input())
m=raw_input().split()
c=len(m)
for i in range(0,c):
	if i%2==0:
		m[i]=int(m[i])
		if m[i]%2!=0:
			print m[i],
	else:
		m[i]=int(m[i])
		if m[i]%2==0:
			print m[i],
