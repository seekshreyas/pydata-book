# IPython log file

get_ipython().system(u'clear ')
get_ipython().magic(u'logstart')
data1 = [6, 7.5, 8., 0., 1.]
import numpy as np
arr1 = np.array(data1)
arr1
get_ipython().system(u'clear ')
data2 = [[1,2,3,4], [5,6,7,8]]
arr2 = np.array(data2)
arr2
arr2.ndim
arr2.shape
arr1.dtype
arr2.dtype
np.zeros(10)
np.zeros((3,6))
np.empty((2,3,2))
np.arange(15)
arr3 = arr2.astype('float64')
arr3
arr2
arr2.dtype
arr3.dtype
arr4 = arr3.astype('int64')
arr4.dtype
arr4
get_ipython().system(u'clear ')
arr4 * arr4
arr4-arr4
1/arr4
arr4
arr4 ** 0.5
arr = np.arange(10)
arr
arr[5:8]
arr[5:8] = 12
arr
arr_slice = arr[5:8]
arr_slice
arr_slice[1]
arr_slice[:]
arr_slice[:] = 64
arr
clea
get_ipython().system(u'clear ')
arr2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
arr2d[2]
arr2d[0][2]
arr2d[0,2]
get_ipython().system(u'clear ')
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = randn(7,4)
arr = np.arange(15).reshape(3,5)
arr
arr.T
arr = np.random.randn(6,3)
np.dot(arr.T, arr)
arr = np.arange(16).reshape((2,2,4))
arr.transpose((1,0,2))
arr.swapaxes(1,2)
get_ipython().magic(u'pinfo np.loadtxt')
get_ipython().magic(u'pinfo np.gentext')
get_ipython().magic(u'pinfo np.genfromtext')
get_ipython().magic(u'pinfo np.genfromtxt')
get_ipython().magic(u'logstop')
