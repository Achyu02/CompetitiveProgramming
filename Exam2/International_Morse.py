def Morse(word,l):	
	d={"A" :".-",
	"B":"-...",
	"C":"-.-.",
	"D" :"-..",
	"E" :".",
	"F" :"..-.",
	"G" :"--.",
	"H" :"....",
	"I" :"..",
	"J":".---",
	"K" :"-.-",
	"L" :".-..",
	"M" :"--",	
	"N" :"-.",
	"O":"---",
	"P" :".--.",
	"Q" :"--.-",
	"R" :".-.",
	"S" :"...",
	"T" :"-",
	"U" :"..-",
	"V" :"...-",
	"W" :".--",
	"X" :"-..-",
	"Y" :"-.--",
	"Z" :"--.."}
	s=""
	for i in word:
		#print(i,"letters in i")
		temp2=i.upper()
		temp=(d.get(temp2))
		#print(temp,s)
		s=s+temp
	l.append(s)

def check(arr):
	l=[]
	for i in arr:
		Morse(i,l)
	#print(l)
	count=0
	## k=[]
	# for i in l:
	# 	o=l.count(i)
	# 	k.append(o)
	d1={}
	count=0
	for i in l:
		if i not in d1:
			d1[i]=1
			count=count+1
	print(count)


	
arr=["gin", "zen", "gig", "msg"]
check(arr)
ar=["a", "z", "g", "m"]
check(ar)
r=["bhi", "vsv", "sgh", "vbi"]
check(r)
rr=["a", "b", "c", "d"]
check(rr)
ap=["hig", "sip", "pot"]
check(ap)