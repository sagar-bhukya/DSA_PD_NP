n=100
li=[]
for i in range(2,int(n**0.5)+1): #here i increments,
     if n%i==0:
          li.append(i)
          while n%i==0: 
               n=n/i # n goes to for loop above
if n!=1:
    li.append(n)
print(li)