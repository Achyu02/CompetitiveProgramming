l=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
k=[]
temp=[]
for i in range(len(l)-2):
	for j in range(i+1,len(l)-1):
		if(l[i][1]<l[j][1]):
			temp.append(l[i])
		elif(l[i][1]==l[j][1]):
			if(l[i][0]<l[j][0]):
				temp.append(l[i])
				temp.append(l[j])
			else:
				temp.append(l[j])
				temp.append(l[i])
		else:
			temp.append(l[j])

print(temp)
