n=int(input())
A=[]
for i in range(n):
    ele=int(input("enter the element"))
    A.append(ele)

for p in range(n-1,0,-1):
    for i in range(p):
        if A[i]>A[i+1]:
            A[i],A[i+1]=A[i+1],A[i]
print(A)

n=6
for i in range(n-1,0,-1):
    print(i)


def bubble_sort(A):
    n=len(A)# n=7
    for tr in range(n-1,0,-1):# n=6
        for i in range(tr):# it runs 6 times
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
    return A
a=bubble_sort([3,5,6,8,9,6,2])
print(a)
