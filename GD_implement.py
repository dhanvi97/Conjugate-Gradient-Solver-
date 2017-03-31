import numpy as np
from numpy import linalg as LA

def linear_iter(A, x, b):
	return np.subtract(b,np.matmul(A,x))

def alpha_calc(r, A):
	'''The 0.1 factor is for coverting to decimal, otherwise returns int later'''
	return (np.matmul(np.transpose(r),r)*0.1)/(np.matmul(np.transpose(r),np.matmul(A,r))*0.1)

if __name__ == '__main__':
	A = np.matrix('3 2;2 6')
	b = np.matrix('2;-8')
	x_0 = np.matrix('0;0')
	x_i = x_0
	r_0 = linear_iter(A,x_0,b)
	r_i = r_0
	i = 0
	epsilon = 0.00000001
	while (LA.norm(r_i) >= epsilon):
		r_i = linear_iter(A,x_i,b)
		'''print(r_i)'''
		alpha = alpha_calc(r_i,A)
		'''print(alpha)'''
		x_i = np.add(x_i,np.multiply(alpha,r_i))
		'''print(x_i)'''
		r_i = np.subtract(r_i,np.multiply(alpha,np.matmul(A,r_i)))
		i += 1
	print(x_i)
	print(i)
	'''Takes 63 iterations for 3x3 example'''
	'''Takes 35 iterations for 2x2 example'''