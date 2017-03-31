import numpy as np
from numpy import linalg as LA

def linear_iter(A, x, b):
	return np.subtract(b,np.matmul(A,x))

def alpha_calc(r, d, A, M):
	'''The 0.1 factor is for coverting to decimal, otherwise returns int later'''
	return (np.matmul(np.transpose(r),np.matmul(LA.inv(M),r))*0.1)/(np.matmul(np.transpose(d),np.matmul(A,d))*0.1)

def beta_calc(r_i1, r_i):
	return (np.matmul(np.transpose(r_i1),np.matmul(LA.inv(M),r_i1)*0.1))/((np.matmul(np.transpose(r_i),np.matmul(LA.inv(M),r_i))*0.1))

if __name__ == '__main__':
	A = np.matrix('2 -1 0;-1 2 -1;0 -1 2')
	b = np.matrix('1;2;3')
	x_0 = np.matrix('0;0;0')
	M = np.matrix('2 0 0;0 2 0;0 0 2')
	'''Taking the matrix as just the diagonal elements of A, (Jacobi preconditioning)'''
	x_i = x_0
	r0 = linear_iter(A,x_0,b)
	d_0 = np.matmul(LA.inv(M),r0)
	r_i = r0
	d_i = d_0
	i = 0
	epsilon = 0.00000001
	while (LA.norm(r_i) >= epsilon):
		'''r_i = linear_iter(A,x_i,b)'''
		'''print(r_i)'''
		alpha = alpha_calc(r_i, d_i, A, M)
		'''print(alpha)'''
		x_i = np.add(x_i,np.multiply(alpha,d_i))
		'''print(x_i)'''
		r_i1 = np.subtract(r_i,np.multiply(alpha,np.matmul(A,d_i)))
		beta = beta_calc(r_i1,r_i)
		r_i = r_i1
		d_i = np.add(np.matmul(LA.inv(M),r_i1),np.multiply(beta,d_i)) 
		i += 1
	print(x_i)
	print(i)
	'''Takes 3 iterations for 3x3 example'''
	'''Takes 2 iterations for 2x2 example'''