#1.Devide the collection of elements into smaller subsets
#2.Recursively sort the subsets
#3.Combine or merge the results into a solution
#4.Devide and conquer approach

def merge(left,right):
    merged=[]
    i=0
    j=0
    while i <len(left) and j < len(right): # traverse the complete 
        if left[i]<=right[j]:
            merged.append(left[i])
            i+=1
        else:
            merged.append(right[j])
            j+=1
    merged += left[i:]+right[j:]
    return merged

def merge_sort(A):
    if len(A)==1:
        return A
    mid=len(A)//2
    left=merge_sort(A[:mid])
    right=merge_sort(A[mid:])
    return merge(left,right)

A=[8,48,582,3,5,2,1]
print(merge_sort(A))


print(0<5)
print(6>12)