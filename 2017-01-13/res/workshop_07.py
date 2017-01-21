"""workshop_07
Creates windows or doors using given parameters
"""

from larlib import *

def resize(x,y,dx,dy):
	'''resizes windows parameters or doors using the given parameters
	@param x : x values of structure's cells
	@param y : y values of structure's cells
	@param dx : resizig x parameter
	@param dy : resizig y parameter'''
	
	sumX=sum(x)
	for i in range(len(x)-2):
		x[i+1]=x[i+1]/(sumX/dx)
	sumY=sum(y)
	for j in range(len(y)-2):
		y[j+1]=y[j+1]/(sumY/dy)
	return(x,y)
	
def ggpl_window(x,y,b):
	'''creates a window using given parameters
	@param x : x values of structure's cells
	@param y : y values of structure's cells
	@param b : matrix indicating wich cells is empty and wich not'''

	def ggpl_window_aux(dx,dy,dz):
		'''@param dx : resizig x parameter
		@param dy : resizig y parameter
		@param dz : resizig z parameter'''

		(xR,yR) = resize(x,y,dx,dy)

		#an empty struct
		struct = STRUCT([CUBOID([0,0,0])])

		accY = 0
		for j in range(len(yR)):
			accX = 0
			for i in range(len(xR)):
				if (b[j][i] == 1):
					cub = CUBOID([x[i],y[j],.05])
					cub = T(1)(accX)(cub)
					cub = T(2)(accY)(cub)
					struct = STRUCT([struct,cub])
				accX += x[i]
			accY += yR[j]
		struct = R([2,3])(PI/2)(struct)
		return struct

	return ggpl_window_aux

def ggpl_door(x,y,b):
	'''creates a door using given parameters
	@param x : x values of structure's cells
	@param y : y values of structure's cells
	@param b : matrix indicating wich cells is empty and wich not'''
	
	def ggpl_door_aux(dx,dy,dz):
		'''@param dx : resizig x parameter
		@param dy : resizig y parameter
		@param dz : resizig z parameter'''

		(xR,yR) = resize(x,y,dx,dy)

		#an empty struct
		struct = STRUCT([CUBOID([0,0,0])])

		accY = 0
		for j in range(len(yR)):
			accX = 0
			for i in range(len(xR)):
				if (b[j][i] == 1):
					cub = CUBOID([x[i],y[j],.05])
					cub = T(1)(accX)(cub)
					cub = T(2)(accY)(cub)
					struct = STRUCT([struct,cub])
				accX += x[i]
			accY += yR[j]

		#color brown
		struct = COLOR(Color4f([205/255.0,170/255.0,125/255.0,1]))(struct)

		#creating the handle
		hx = sum(x)/10.0
		hy = sum(y)/40.0
		hPosition = sum(x[2:])+x[0]*3.0/2.0
		handle = CUBOID([hx,hy,(dz*2.0)/2.0])
		handle = T([1,2])([hPosition,sum(y)/2.0])(handle)

		struct = STRUCT([struct,handle])
		struct = R([2,3])(PI/2)(struct)
		return struct

	return ggpl_door_aux

def main():

	xw=[.05,1,.05,1,.05,1,.05]
	yw=[.05,1.2,.1,.7,.05]
	bw=[[1,1,1,1,1,1,1],[1,0,1,0,1,0,1],[1,1,1,1,1,1,1],[1,0,1,0,1,0,1],[1,1,1,1,1,1,1]]
	VIEW(ggpl_window(xw,yw,bw)(1.8,2,.1))

	xd=[.06,.07,.12,.09,.06]
	yd=[.2,.2,.2,.2,.2,.2,.2]
	bd=[[1,1,1,1,1],[1,1,0,0,1],[1,1,1,1,1],[1,0,0,1,1],[1,1,1,1,1],[1,1,0,0,1],[1,1,1,1,1]]
	VIEW(ggpl_door(xd,yd,bd)(1.8,2,.1))


if __name__=='__main__':
	main()
