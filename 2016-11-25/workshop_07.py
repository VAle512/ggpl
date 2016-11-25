"""workshop_07
Creates windows or doors using given parameters

"""

from larlib import *

def ggpl_windows_and_doors(x,y,b):
	'''creates windows or dorrs using given parameters
	@param x : x values of structure's cells
	@param y : y values of structure's cells
	@param b : matrix indicating wich cells is empty and wich not'''

	#a NULL struct
	s = STRUCT([CUBOID([0,0,0])])
	
	accY = 0
	for j in range(len(y)):
		accX = 0
		for i in range(len(x)):
			if (b[j][i] == 1):
				c = CUBOID([x[i],y[j],.05])
				c = T(1)(accX)(c)
				c = T(2)(accY)(c)
				s = STRUCT([s,c])
			accX += x[i]
		accY += y[j]

	VIEW(s)


def main():
	x = [.05,.7,.05,.7,.05]
	y = [.05,.7,.05,.7,.05]
	b = [[1,1,1,1,1],[1,0,1,0,1],[1,1,1,1,1],[1,0,1,0,1],[1,1,1,1,1]]

	ggpl_windows_and_doors(x,y,b)


if __name__ == '__main__': 
	main()
