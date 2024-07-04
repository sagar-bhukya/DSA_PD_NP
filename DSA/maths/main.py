#digit concepts
#7789
# a=7789
# b=a/10
# print(b%10)
b=[]
a=7789
while(a>0):
    last_digit=a%10
    b.append(last_digit)
    a=a//10
print(b)



#check palindrome
def isPalindrome(x: int) -> bool:
        original=x
        rev=0
        while(x>0):
            last=x%10
            rev=(rev*10)+last
            x=x//10
        if rev==original:
            return True
        else:
            return False

print(isPalindrome(7))


#armstrong numbers
def armstrongNumber (n):
        # code here 
        original=n
        cube=0
        while n>0:
            l=n%10
            cube += l**3
            n=n//10
        if cube==original:
            return 'true'
        else:
            return 'false'
print(armstrongNumber(6))


import maths
#factors of a number
n=36
# for i in range(1,n+1):
#      if n%i==0:
#           print(i)

for i in range(1,int(n**0.5)+1):
     if n%i==0:# 36%1==0
          print(i)#1
          if n//i !=i: #36//1 !=1
               print(n//i)

#sum of all factors
a=4
s=0
for i in range(1,a+1):
     if a%i==0:
          s += i
print(s)
     


#check prime numbers
n = 2
c = 0
#brute force method
for i in range(1, int(n**0.5) + 1):
    if n % i == 0:
        c += 1
        if n // i != i:  # Check for the second divisor, if it's not the square root of n
            c += 1

if c == 2:
    print('true')
else:
    print('false')
   



#GCD or HCF of two numbers

# n1,n2=9,12
n1,n2=20,10
gcd=1
# for i in range(1,n1+1):
for i in range(1,min(n1,n2)+1):
     if n1%i==0 and n2%i==0:
          gcd=i
print(gcd)




gcd=0
n1,n2=9,12
for i in range(min(n1,n2),0,-1):
     if n1%i==0 and n2%i==0:
          gcd=i
          break    
print(gcd)
lcm=(n1*n2)/gcd
print(lcm)

a=(9*12)/3
print(a)




#print all divisors of a number 36 srore them in a list

'''
li=[]
n=36
for i in range(1,n+1):
     if n%i==0:
          li.append(i)
print(li)#[1, 2, 3, 4, 6, 9, 12, 18, 36]
'''

li=[]
n=36
for i in range(1,int(n**0.5)+1):
     if n%i==0:
          li.append(i)
          if n/i !=i:
               li.append(int(n/i))
print(li)#[1, 36, 2, 18, 3, 12, 4, 9, 6]


#check the prime number condition:  it has only two divisors 1 and number itself
n=int(input())
c=0
for i in range(1,int(n**0.5)+1):
     if n%i==0:
          print(i)
          c=c+1
          if n/i!=i:
               print(n//i)
               c=c+1
if c==2:
     print("prime number")
else:
     print("not prime number")

    
#print all prime factors of a number
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


#find all the prime numbers from 1-100
