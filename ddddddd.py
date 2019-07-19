c2,28=map(int,input().split())
char=input().split()
b=[]
for i in char:
	if(int(i)%2!=0):
		b.append(i)
print(b[28-1])
