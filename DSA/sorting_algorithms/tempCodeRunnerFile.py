def bubble_sort(A):
    n=len(A)
    for tr in range(n-1,0,-1):
        for i in range(tr):
            if A[i]>A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
    return A
a=bubble_sort([3,5,6,8,9,6,2])
print(a)