import numpy as np
from numpy import linalg as LA
import sympy as sp


def linear_iter(A, x, b):
	return np.subtract(b,np.matmul(A,x))

def alpha_calc(r, d, A):
	'''The 0.1 factor is for coverting to decimal, otherwise returns int later'''
	return (np.matmul(np.transpose(r),r)*0.1)/(np.matmul(np.transpose(d),np.matmul(A,d))*0.1)

def beta_calc(r_i1, r_i):
	return (np.matmul(np.transpose(r_i1),r_i1)*0.1)/((np.matmul(np.transpose(r_i),r_i))*0.1)

if __name__ == '__main__':
	i = 0
	k = 0
	#Function definition#
	x, y, z = sp.symbols("x y z")
	fun = 5*x**2 - 3*x
	gradfun = [sp.diff(fun, var) for var in (x, y, z)]
	numgradfun = sp.lambdify([x, y, z], gradfun)
	# Function definition ends
	grad2funx = sp.lambdify([x, y, z], [sp.diff(gradfun[0], var) for var in (x, y ,z)])
	grad2funy = sp.lambdify([x, y, z], [sp.diff(gradfun[1], var) for var in (x, y ,z)])
	grad2funz = sp.lambdify([x, y, z], [sp.diff(gradfun[2], var) for var in (x, y ,z)])
	#hessian = np.matrix([grad2funx, grad2funy, grad2funz]) 
	# Negative gradient
	s = np.matrix("0.5;0;0")
	r = np.multiply(-1,np.transpose(np.matrix(numgradfun(s.item(0),s.item(1),s.item(2)))))
	d = r
	del_new = np.matmul(np.transpose(r),r)
	del_0 = del_new
	i_max = 80
	j_max = 5
	epsilon = 0.0001
	eps_nr = 0.00001
	while (del_new >= epsilon**2*del_0 or i<i_max):
		j = 0
		del_d = np.matmul(np.transpose(d),d)
		while True:
			alpha = -1.*((np.matmul(np.matrix(numgradfun(s.item(0),s.item(1),s.item(2))),d)*0.1)/np.matmul(np.transpose(d),np.matmul(np.matrix([grad2funx(s.item(0),s.item(1),s.item(2)),grad2funy(s.item(0),s.item(1),s.item(2)),grad2funz(s.item(0),s.item(1),s.item(2))]),d)))
			s = s + np.multiply(alpha,d)
			j += 1
			if (alpha**2*del_d > eps_nr**2 or j < j_max):
				break
		r = np.multiply(-1,np.transpose(np.matrix(numgradfun(s.item(0),s.item(1),s.item(2)))))
		print(s)
		del_old = del_new
		del_new = np.matmul(np.transpose(r),r)
		beta = (del_new*0.1)/(del_old*0.1)
		d = np.add(r, np.multiply(beta, d))
		k += 1
		if (k == 3 or np.matmul(np.transpose(r),d) <= 0):
			d = r
			k = 0
		i += 1
	print(i)
	'''Takes 3 iterations for 3x3 example'''
	'''Takes 2 iterations for 2x2 example'''