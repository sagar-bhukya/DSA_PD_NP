def partition(A,low,high):
    pivot=A[low]
    i=low
    j=high
    while True:
        while i<=j and A[i] <= pivot:
            i=i+1

        while i<=j and A[j]>pivot:
            j=j-1
        if i<=j:
            A[i],A[j]=A[j],A[i]
        else:
            break
    A[low],A[j]=A[j],A[low]
    return  j #partition 4

def quick_sort(A,low,high):
    if low<high:
        pi=partition(A,low,high)#4
        quick_sort(A,low,pi-1)#(A,0,4-1)
        quick_sort(A,pi+1,high)#(A,4+1,6)


A=[8,3,6,4,9,2,9]
print("original array\n",A)
quick_sort(A,0,len(A)-1)
print(A)






#realtime application:Sorting Products by Price in an E-commerce Platform
class Product:
    # Product class to store product name and price
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # String representation of the Product object for easy printing
    def __repr__(self):
        return f"{self.name}: ${self.price:.2f}"

def partition(products, low, high):
    # Choose the pivot element (the first element in the current segment)
    pivot = products[low].price
    i = low
    j = high
    while True:
        # Move i to the right until an element greater than the pivot is found
        while i <= j and products[i].price <= pivot:
            i += 1
        # Move j to the left until an element less than or equal to the pivot is found
        while i <= j and products[j].price > pivot:
            j -= 1
        # If i is still less than or equal to j, swap the elements at i and j
        if i <= j:
            products[i], products[j] = products[j], products[i]
        else:
            # If i and j have crossed, break the loop
            break
    # Place the pivot element in its correct sorted position
    products[low], products[j] = products[j], products[low]
    # Return the index of the pivot element
    return j

def quick_sort(products, low, high):
    # Recursively apply Quick Sort to the partitions
    if low < high:
        # Partition the array and get the pivot index
        pi = partition(products, low, high)
        # Recursively sort the elements before and after the partition
        quick_sort(products, low, pi - 1)
        quick_sort(products, pi + 1, high)

# List of products with name and price
products = [
    Product("Laptop", 999.99),
    Product("Smartphone", 599.99),
    Product("Tablet", 399.99),
    Product("Headphones", 199.99),
    Product("Smartwatch", 299.99)
]

print("Original list of products:")
for product in products:
    print(product)

# Sort products by price using Quick Sort
quick_sort(products, 0, len(products) - 1)

print("\nSorted list of products by price:")
for product in products:
    print(product)
