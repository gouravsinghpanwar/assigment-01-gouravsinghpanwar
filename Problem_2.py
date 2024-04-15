""" 

Problem: Knock Knock are you there?

Input Format:

1. Take M int input from the User 
2. Get M , seperated values from a user 
3. Enter a number 'N' you are looking for

Output Format:

1. Print index on console once Found or Print 'Better Luck Next Time' to the console


"""
m= int(input())
n= str(input())
a= []
x= ''
for i in n:
    if i== ',':
        a.append(x)
        x= ''
    else:
        x= x+i
a.append(x)
N=input()
if N in a:
    print(len(a)-1-a[::-1].index(N))
else:
    print('Better Luck Next Time') 
