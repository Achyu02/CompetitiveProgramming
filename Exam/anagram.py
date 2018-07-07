def anagram(s,t):
	flag=1
	s=s.lower()
	t=t.lower()
	for i in t:
		if i in s:
			continue
		if(i==" " or i=="," or i=="@" or i=="."):
			continue
		else:
			flag=0
	if(flag==0):
		print("false")
	elif(flag==1):
		print("true")


anagram("anagram","nagaram")
anagram("Keep","Peek")
anagram("Mother In Law", "Hitler Woman")
anagram("School Master","The Classroom")
anagram("ASTRONOMERS","NO MORE STARS")
anagram("Toss","Shot")
anagram("joy","enjoy")
anagram("Debit Card","Bad Credit")
anagram("SiLeNt CAT","LisTen AcT")
anagram("Dormitory","Dirty Room")

