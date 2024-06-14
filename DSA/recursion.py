#base case of condition
#square of n numbers using recursion
print("square of n numbers using recursion")
def fun(n):#4,3
    if n>0:#4>0,3>0
        k=n**2#16,9
        print(k)
        fun(n-1)#(4-1=3),(3-1=2) func call itself until n==0
fun(4)

#square of n numbers normal
print("square of n numbers")
for i in range(1,5):
    s=i**2
    print(s)

def sq(n):
    if n>0:
        i=1
        while i<=n:
            s=i**2
            print(s)
            i+=1
sq(4)

#-----
print("sum of n natural numbers using recursion")
def sum_rec(n):
    if n==1:
        return 1
    return sum_rec(n-1)+n
print(sum_rec(4))

print("factorial n using recursion")
def fact_rec(n):
    if n==0:
        return 1
    return fact_rec(n-1)*n
print(fact_rec(4))
