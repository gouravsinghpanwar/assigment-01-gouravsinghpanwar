"""
Given a list of length M, you need to print and find sum of the elements of list 

Input Format :

Line 1 : An int M 
Line 2 : M int elements of list seperated by ';'

Output Format:

Addition 

Constraints :
1 <= M <= 10^6

"""
m =int(input())
n =input()
a =[]
b =''  
for i in n:
    if i !=';':
        b =b+i
    else:
        a.append(int(b))
        b =''
if b:
    a.append(int(b))
c = a[::1]
total = 0
for b in c:
    total =total+b
print(total)
