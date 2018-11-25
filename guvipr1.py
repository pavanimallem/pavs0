s=raw_input()
s1=raw_input()
l=[]
for i in range(0,len(s)):
    if s[i]==s1[i]:
    	l.append(s[i])
print"".join(l)
