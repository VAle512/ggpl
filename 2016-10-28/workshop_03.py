"""workshop_03.py

Creates two different images of an u-shaped stair inside and invisible box, given two different sets of actual parameters.
"""
from larlib import *

def ggpl_u_shaped_stair_support(dx,dy,dz,stepsNumber):
	"""
	function that creates a u shaped stairs inside a box according to given parameters (measures are supposed to be in centimeters)

	@param dx: box's length
	@param dy: box's width
	@param dz: box's height
	@param stepsNumber: number of steps per flight
	"""

	#creates a single step
	stepX=dx/2
	stepY=dy/(stepsNumber*2)
	stepZ=dz/11
	step=CUBOID([stepX,stepY,stepZ])
	flight1=step

	#creates the first flight
	accZ=stepZ
	accY=stepY
	while accZ<(stepZ*stepsNumber):
		stepTemp=T(2)(accY)(step)
		accY+=stepY
		flight1=STRUCT([flight1,T(3)(accZ),stepTemp])
		accZ+=stepZ

	#creates the platform and links it to the first flight
	platform=CUBOID([dx,stepsNumber*stepY,stepZ])
	platform=T(2)(accY)(platform)
	stairs=STRUCT([flight1,T(3)(accZ),platform])
	accZ+=stepZ

	#creates the second flight
	flight2=flight1	
	flight2=R([1,2])(PI)(flight2)
	flight2=T(1)(stepX*2)(flight2)
	flight2=T(2)(stepsNumber*stepY)(flight2)
	flight2=T(3)(accZ)(flight2)
	stairs=STRUCT([stairs,flight2])	

	#creates the box
	box = SKEL_1(BOX([1,2,3])(stairs))

	#creates and visualizes the structure
	VIEW(STRUCT([stairs, box]))

def ggpl_u_shaped_stair(dx,dy,dz):
	"""
	function that creates a u shaped stairs inside a box according to given parameters (in meters) and 8 steps per flight

	@param dx: box's length
	@param dy: box's width
	@param dz: box's height	
	"""

	#trasforms the given parameters from meters to centimeters
	dxCm = dx * 100
	dyCm = dy * 100
	dzCm = dz * 100

	stepsNumber = 8

	ggpl_u_shaped_stair_support(dxCm,dyCm,dzCm,stepsNumber)

if __name__=='__main__':
	ggpl_u_shaped_stair(2,5,3.5)
	ggpl_u_shaped_stair(2,9,5)
