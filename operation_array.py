import numpy as np
print('8.concatenate(a,b) gives full in one array')
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(a,'\n',b)
'''
[[1 2]
 [3 4]] 
 [[5 6]
 [7 8]]
'''
print('concatenate(a,b)\n',np.concatenate((a,b),axis=1))
'''
 [[1 2 5 6]
 [3 4 7 8]]
'''
print('concatenate(a,b)\n',np.concatenate((a,b),axis=0))
'''
 [[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''

print('stack( ) also act same as concatenate but not in one array')
print('stack(a,b)\n',np.stack((a,b),axis=0))
'''
axis=0 default for row
output:
 [[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
'''
print('stack(a,b)\n',np.stack((a,b),axis=1))
'''
 [[[1 2]
  [5 6]]

 [[3 4]
  [7 8]]]
'''
print('9.vstack()-> vertical stack')
print('vstack(a,b)\n',np.vstack((a,b)))
''' 
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
 '''
print('10.hstack()-> horizontal stack')
print('hstack(a,b)\n',np.hstack((a,b)))
'''
 [[1 2 5 6]
 [3 4 7 8]]
'''
print('11.dstack()->d stack')
print('dstack(a,b)\n',np.dstack((a,b)))
'''
 [[[1 5]
  [2 6]]

 [[3 7]
  [4 8]]]
'''
print('12. split()-> into parts')
c=np.arange(1,9)
print(c)
d=np.split(c,2)
print(d)
s1,s2,s3,s4=np.split(c,4)
for i in s1,s2,s3,s4:
    print(i)
print('13.2-D where() is to find the ele')
d=np.arange(10,130,10).reshape(4,3)
print(d)
'''
[[ 10  20  30]
 [ 40  50  60]
 [ 70  80  90]
 [100 110 120]]
'''
print('where(d==80)\n',np.where(d==80))# (array([2], dtype=int64), array([1], dtype=int64))

print('1-D where()')
d1=np.arange(10,130,10)
print(d1)#[ 10  20  30  40  50  60  70  80  90 100 110 120]
print('1-D where(d1=60)\n',np.where(d1==60))#(array([5], dtype=int64),)

print('where(expression ex: a%20==0)')
d3=np.arange(10,130,10).reshape(4,3)
print(d3)
print('where(expresion)\n',np.where(d3%2==0))

print('Arithmatic operations-------should have equal dimensions like a=2x3 b=2x3---------')
print('1.add(a,b)')
a1=np.array([[1,2,3],[4,5,6]])
a2=np.array([[10,20,30],[40,50,60]])
print(a1,'\n',a2)
print('add(a1,a2)\n',np.add(a1,a2))

print('subtract(a,b)----')
print('subtract(a1,a2)\n',np.subtract(a2,a1))

print('multiply(a1,a2)')
print('multiply(a1,a2)\n',np.multiply(a1,a2))

print('divide(a1,a2)\n',np.divide(a1,a2))
print('exp(sigle argument)\n',np.exp(a1))
print('sqrt(a)\n',np.sqrt(a1))
print('comparision(a1==a2)\n',a1==a2)

print('array functions--------------')
x=np.array([[1,2,3],[4,5,6]])
print('x\n',x)
print('1.sum(x)-> sum of all ele\n',np.sum(x))
print('2.min(x)->gives min ele from x array\n',np.min(x))
print('3.max()->gives max ele from the x array\n',np.max(x))
print('4.mean(x)->gives mean value of x array. mean=sum of all/no.of elem\n',np.mean(x))
print('4.median(x)->gives mid value of x array\n',np.median(x))

