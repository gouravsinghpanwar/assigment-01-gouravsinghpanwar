m=int(input())
n=str(input())
def reflection():
    a=[]
    b=''
    for i in n:
        if i !=",":
            b=b+i
        else:
            a.append(b)
            b=''
    if b:
        a.append(b)                 
    c=a[::-1]
    for b in c:
        print(b)
reflection()
