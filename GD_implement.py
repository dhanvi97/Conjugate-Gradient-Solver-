import numpy as np
from numpy import linalg as LA

def linear_iter(A, x, b):
	return np.subtract(b,np.matmul(A,x))

def alpha_calc(r, A):
	return (np.matmul(np.transpose(r),r)*0.1)/(np.matmul(np.transpose(r),np.matmul(A,r))*0.1)

if __name__ == '__main__':
	A = np.matrix('4 1;1 3')
	b = np.matrix('1;2')
	x_0 = np.matrix('0;0')
	x_i = x_0
	r_0 = linear_iter(A,x_0,b)
	r_i = r_0
	epsilon = 0.00000000000001
	while (LA.norm(r_i) >= epsilon):
		r_i = linear_iter(A,x_i,b)
		'''print(r_i)'''
		alpha = alpha_calc(r_i,A)
		'''print(alpha)'''
		x_i = np.add(x_i,np.multiply(alpha,r_i))
		'''print(x_i)'''
		r_i = np.subtract(r_i,np.multiply(alpha,np.matmul(A,r_i)))
	print(x_i)