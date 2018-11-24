n=int(raw_input())
list=[int(x) for x in raw_input().split()]
for i in list:
	count=0
	for j in list:
		if(i==j):
			count+=1
	if(count==1):
		print i
			
