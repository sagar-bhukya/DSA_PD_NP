# #iterative way
# print('iterative way')
# A=[4,7,9,15,20]
# key=15
# def binary_iter(A,key):
#     L=0
#     R=len(A)-1
#     while L<=R:
#         M=(L+R)//2
#         if key==A[M]:
#             return M
#         elif key<A[M]:
#             R=M-1
#         elif key>A[M]:
#             L=M+1
#     return 'Not found'
# print(binary_iter(A,key))



#array search with realtime application
def shopping_cart():
    """Simulates a simple online shopping cart using arrays.

    Allows users to add products (ID, name, price) to the cart,
    display cart contents, and calculate the total price.
    """

    # Array to store product information (ID, name, price)
    product_ids = []
    product_names = []
    product_prices = []

    while True:
        id = int(input("Enter product ID (or -1 to finish): "))
        if id == -1:
            break

        name = input("Enter product name: ")
        price = float(input("Enter product price: "))

        product_ids.append(id)
        product_names.append(name)
        product_prices.append(price)

    # Display cart contents and calculate total price
    print("\nYour shopping cart:")
    total_price = 0.0
    for i in range(len(product_ids)):
        print(f"  - {product_ids[i]} ({product_names[i]}): ${product_prices[i]:.2f}")  # Format price with 2 decimal places
        total_price += product_prices[i]

    print("\nTotal price: ${:.2f}".format(total_price))  # Format total price with 2 decimal places


shopping_cart()



