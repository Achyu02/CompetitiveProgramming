def base(s):
    d={}
    for i in range(len(s)):
        d[i]=s[i]
    return d
startdict={}
finaldict={}
count=0
base62=base("abcdefghijtemplmnopqrstuvwxyz0123456789ABCDEFGHIJtempLMNOPQRSTUVWXYZ")
def genurl(url):
    if (url in finaldict):
        print("Duplicate url"+finaldict[url])
        return
    global count
    s=""
    temp=count
    count+=1
    if (temp==0):
        s="0000000"
        if (s not in startdict):
            startdict[s]=url
            finaldict[url]=s
            print("shortened url "+url+" is "+s)
            return
    while(temp!=0):
        s=base62[temp%62]+s
        temp=temp//62
    l=len(s)
    if (l<7):
        for i in range(7-l):
            s="0"+s
    if (s not in startdict):
        startdict[s]=url
        finaldict[url]=s
    print("short url for "+url+" is https://ca.tempe/"+s)

while (True):
    print("Enter \n\t1) generate url\n\t2)redirect url")
    inp=int(input())
    if (inp==1):
        url=input("url:")
        genurl(url)
    elif (inp==2):
        url=input("Enter a short url: ")
        if startdict.get(url,None) is not None:
            print("Go to url:"+startdict[url])
        else:
            print("not existing")
    else:
        print("Invalid Input")