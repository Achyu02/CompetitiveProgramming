def func(l,p):
	if(p==len(l)):
		return
	for j in range(len(l[p])):
		v=l[p][j]
		if v in temp:
			continue
		else:
			temp.append(v)
			# print("appending",temp)
			return func(l,v)

l=[[1], [2,3], [1,2], [4], [1], [5]]
temp=[0]
func(l,0)
# print(temp)
a=[]
for z in l:
	for p in z:
		a.append(p)
# print(a)
flag=1
for i in a:
	if i in temp:
		continue
	else:
		flag=0
if(flag==0):
	print("false")
elif(flag==1):
	print("true")
