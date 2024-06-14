# def linear(A,key):
#     index=0
#     while index<len(A):
#         if A[index]==key:
#             return index
#         index+=1
#     return -1
# A=[80,47,30,50]
# key=30
# print(linear(A,key))


# realtime example
def find_product_by_id(products, product_id):
  """
  This function searches for a product with a specific ID in a list of products.

  Args:
      products: A list of dictionaries, where each dictionary represents a product
          with keys like "id", "name", "price", etc.
      product_id: The ID of the product to search for.

  Returns:
      The product dictionary if found, None otherwise.
  """

  for product in products:
    if product["id"] == product_id:
      return product
  return None

# Example usage
products = [
  {"id": 1, "name": "T-Shirt", "price": 19.99},
  {"id": 2, "name": "Jeans", "price": 39.99},
  {"id": 3, "name": "Sweatshirt", "price": 24.99},
]

product_to_find = int(input("Enter the product ID to search: "))
found_product = find_product_by_id(products, product_to_find)

if found_product:
  print("Product found:")
  print(f"  ID: {found_product['id']}")
  print(f"  Name: {found_product['name']}")
  print(f"  Price: ${found_product['price']:.2f}")
else:
  print("Product not found.")
