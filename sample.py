#1.install numpy
#pip install numpy
import numpy as np
#creatig array
a=np.array([10])
print(a)
#1D array
b=np.array([10,20,30])
print(b)
#2d array
c=np.array([[10,20],[1,2]])
print(c)
#access
print(c[1][0])

#3D array
d=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d)
#access 6
print(d[1][0][1])

#asarray() with nditer()
x=[10,20,30]
y=np.asarray(x,dtype=float)
print(y)
#with nditer
#row major order-"C"
print('row major order')
a1=[[10,20],[30,40]]
b1=np.asarray(a1,dtype=int,order="C")
for i in np.nditer(b1):
    print(i)
#column major order-"F"
print('column major order')
a2=[[10,20],[30,40]]
b2=np.asarray(a2,dtype=int,order="F")
for i in np.nditer(b2):
    print(i)


print('frombuffer()--------')
st=b"Welcome to Google"    #S1 means string datatype
c1=np.frombuffer(st,dtype='S1',count=4,offset=5)#[b'm' b'e' b' ' b't']
print(c1)


print('fromiter()___________')
a3=[1,2,3,4,5,6]
a5=np.fromiter(a3,dtype='S1',count=3)#[b'1' b'2' b'3']
print(a5)



print("--------------array initialisation----------------")
print('zeros() -deafault prints 0 floats')
print('1-d')
x1=np.zeros(3)
print(x1)
print('2-D---------')
x2=np.zeros([2,3])
print(x2)

print('3-D------')
x3=np.zeros([2,3,3])
print(x3)

print('full()-([a,b],value to be replaced) without float and comma')
print('1-D')
y2=np.full([3],1)
print(y2)
print('2-D**********')
y1=np.full([2,3],2)
print(y1)
print('3-D ________')
y3=np.full([2,3,4],7)
print(y3)


print('3.random.rand()->  it generates random float values from 1-9,starts with 0 ex:0.98765432 here float value must 8')
print('here we need not give any value we just give dimension')
print('1D array-----')
z1=np.random.rand(3)
print(z1)
print('2-D array of random.rand(2,3)')
z2=np.random.rand(2,3)
print(z2)
print('3-D array of random.rand(2,3,4)')
z3=np.random.rand(2,3,4)
print(z3)

print('4.ones()-> it returns default with 1 float')
print('1-D of ones(4)')
n1=np.ones(5)
print(n1)
print('2-D ones(2,3)')
n2=np.ones([2,3])
print(n2)
print('3-D of ones(2,3,4)')
n3=np.ones([2,3,4])
print(n3)

print('5.eye()-diagonal matrix check, so we need square matrix. default value of diagonal is 0.')
print('we pass one argument only. ex eye(2)-2x2 matrix that is square matrix')
print('1-D')
m1=np.eye(1)
print(m1)
print('2-D of eye(2)')
m2=np.eye(2)
print(m2)
print('3-D eye(3)')
m3=np.eye(3)
print(m3)

print('Numerical-ranges----')
d1=np.arange(1,7,1)#same as range
print(d1)
#we need to change that in multi-dimensional
print('reshape()---- only for equal divison')
d2=d1.reshape(2,3)
print(d2)
print(d1.reshape(3,2))

print('linespace(start,stop,intervals,endpoint=True->stop value included,retstep=True->gives difference btw 2 numbers)')
e1=np.linspace(0,100,20,endpoint=False,retstep=True)#endpoint=False->stop value excluded
print(e1)

print('logspace(start,stop,interval,base->default 10)')
l=np.logspace(1,10,5,base=2)
print(l)

print('array properties')
'''
np.size(array)-Size of the array
np.shape(array)-Dimension of the array ex:(2,3),(3,3)
array.dtype()-Type of array
'''
ar=np.arange(10,100,10)
print(ar)
ar=ar.reshape(3,3)
print(ar)
print("size of ar: ",np.size(ar))
print("shape of ar: ",np.shape(ar))
print("dtype of ar: ",ar.dtype)


#array operations
print('array operations----')
print('1.accessing array')
i=np.array([[1,2,3],[4,5,6]])
print(i[0])
print(i[1][2])

print('2.slicing***')
s=np.arange(10,100,10)
print(s)#[10 20 30 40 50 60 70 80 90]
print(s[2:5])#[30 40 50]

print('3.copy()->copy one array to other array')
s1=np.copy(s)
print(s1)
print('view()-> same as copy but act as reference. If we change the owner of this, it will also can change')
s2=s1.view()
print(s2)
print('now update the s1, automatically s2 also updated')
s1[3]=99
print('s1 updated: ',s1)
print('view s2 also updated: ',s2)

print('4.sort()--')
print('1-D array sort')
sr=np.array([9,3,5,2,4,7])
print(np.sort(sr))
print('2-D array of sort')
sr2=np.array([[4,5,3],[1,8,6]])
print(sr2)
print('sort by default axis=1-> for row wise\n',np.sort(sr2))
print('sort with axis=0 for column wise\n',np.sort(sr2,axis=0))

print('---------------')
print('5.reshape()-> ')
r=np.arange(10,130,10)
print(r)#12 ele-> [ 10  20  30  40  50  60  70  80  90 100 110 120]
print("2-D reshape(2,6)\n",r.reshape(2,6))# 2-rows 6-columns
print('3-D reshape(2r,3sub,2col)\n',r.reshape(2,3,2))

print('6.append()->it returns only 1-D array')
ap=np.array([1,2,3,4])
apd=np.array([5,6,7,8])
print('append--\n',np.append(apd,ap))#[5 6 7 8 1 2 3 4]
ap1=np.array([[1,2],[3,4]])
apd1=np.array([[5,6],[7,8]])
print('2-D append gives 1-D array--\n',np.append(ap1,apd1))# [1 2 3 4 5 6 7 8]
print('change that 1-D array to multiD with reshape(4,2)--\n',np.append(ap1,apd1).reshape(2,4))#[[1 2 3 4]
                                                                                               #[5 6 7 8]]

print('7.insert(array,index,ele)-> returns 1-D')
p1=np.array([[1,2],[3,4]])
print(p1)
print('insert(p1,3,99)\n',np.insert(p1,3,99))# [ 1  2  3 99  4]
print('for multiple values insert, insert(p1,3,[40,41,42])\n',np.insert(p1,3,[40,41]).reshape(3,2))#[ 1  2  3 40 41 42  4]

print('8.delete(array,index-to be deleted)------------------------')
d=np.array([[1,2],[3,4]])
print(d)
print('delete(d1,index) \n',np.delete(d,2))

print('go to operation_array folder----------------------------------------------end')
