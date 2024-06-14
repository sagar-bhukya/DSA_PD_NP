#iterative way
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

