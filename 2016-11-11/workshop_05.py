'''workshop_05.py

creates a classroom with a blackboard, a teacher desk and some desks inside
'''

from larlib import *

def ggpl_blackboard(dx,dy,dz):
	'''creates a blackboard with given dimentions'''

	#creates a whiteboard
	blackboard = CUBOID([dx,dy,dz])
	#creates the frame of the final structure
	frame = OFFSET([.1,.1,.1])(SKEL_1(blackboard))
	#paints the whiteboard black
	blackboardC = COLOR(BLACK)(blackboard)

	return(STRUCT([blackboardC,frame]))

def ggpl_desk(dx,dy,dz):
	'''creates a desk with given dimentions'''

	#radius of a single leg
	r = 0.05

	#creates all four legs
	leg = CYLINDER([r,dz])(100)
	leg = COLOR(GRAY)(leg)
	desk = leg
	desk = STRUCT([desk,T([1,2,3])([dx,0,0]),leg])
	desk = STRUCT([desk,T([1,2,3])([0,dy,0]),leg])
	desk = STRUCT([desk,T([1,2,3])([dx,dy,0]),leg])

	#creates the plane of the desk
	plane = CUBOID([dx+(r*2),dy+(r*2),.075])
	plane = COLOR(CYAN)(plane)
	desk = STRUCT([desk,T([1,2,3])([-r,-r,dz]),plane])

	#creates a second plane under the main one
	underPlane = CUBOID([dx+(r*2),dy+(r*2),.05])
	underPlane = COLOR(GRAY)(underPlane)
	desk = STRUCT([desk,T([1,2,3])([-r,-r,(dz*5)/7]),underPlane])

	return(desk)

def ggpl_chair(dx,dy,dz):
	'''creates a chair with given dimentions'''

	#radius of a single leg
	r = 0.025

	#creates all four legs
	legFront = CYLINDER([r,dz/3.0])(100)
	legFront = COLOR(GRAY)(legFront)
	legBack = CYLINDER([r,(dz*3.0)/4.0])(100)
	legBack = COLOR(GRAY)(legBack)
	chair = legBack
	chair = STRUCT([chair,T([1,2,3])([dx,0,0]),legFront])
	legBack = CYLINDER([r,(dz*3.0)/4.0])(100)
	legBack = COLOR(GRAY)(legBack)
	chair = STRUCT([chair,T([1,2,3])([0,dy,0]),legBack])
	chair = STRUCT([chair,T([1,2,3])([dx,dy,0]),legFront])

	#creates the sitting plane
	sit = CUBOID([dx+(r*2),dy+(r*2),.05])
	sit = COLOR(Color4f([205/255.0,170/255.0,125/255.0,1]))(sit)
	chair = STRUCT([chair,T([1,2,3])([-r,-r,dz/3.0]),sit])

	#creates the back of the chair
	back = CUBOID([.05,dy+(r*2),dz/4.0])
	back = COLOR(Color4f([205/255.0,170/255.0,125/255.0,1]))(back)
	chair = STRUCT([chair,T([1,2,3])([-r,-r,(dz*3.0)/4.0]),back])

	return(chair)

def ggpl_desk_chair(dx,dy,dz):
	'''put together a desk with the given dimentions and two chairs'''

	desk = ggpl_desk(dx,dy,dz-.3)
	desk = T(2)(0.2)(desk)
	chair = ggpl_chair((dx/3),(dy/2),dz)
	chair = R([1,2])(PI/2)(chair)
	chair1 = T(1)(dx*3/4+.1)(chair)
	chair2 = T(1)(dx*2/4-.1)(chair)
	deskChair = STRUCT([desk,chair1,chair2])
	
	return(deskChair)

def ggpl_teacher_desk(dx,dy,dz):
	'''creates a teacher desk with the given dimentions'''

	#radius of a single leg
	r = 0.07

	#creates all four legs
	leg = CYLINDER([r,dz])(100)
	leg = COLOR(GRAY)(leg)
	desk = leg
	desk = STRUCT([desk,T([1,2,3])([dx,0,0]),leg])
	desk = STRUCT([desk,T([1,2,3])([0,dy,0]),leg])
	desk = STRUCT([desk,T([1,2,3])([dx,dy,0]),leg])

	#creates the plane of the desk
	plane = CUBOID([dx+(r*2),dy+(r*2),.075])
	plane = COLOR(CYAN)(plane)
	desk = STRUCT([desk,T([1,2,3])([-r,-r,dz]),plane])

	return(desk)

def ggpl_teacher_desk_chair(dx,dy,dz):
	'''put together a teacher desk with the given dimentions and a chair'''

	desk = ggpl_teacher_desk(dx,dy,dz-.3)
	desk = T(2)(0.2)(desk)
	chair = ggpl_chair((dx/3.0),(dy/2.0),dz)
	chair = R([1,2])(PI/2)(chair)
	chair = T(1)(dx*2/3)(chair)
	deskChair = STRUCT([desk,chair])
	
	return(deskChair)

def ggpl_classroom(dx,dy,dz):
	'''creates a classroom with the given dimentions with a blackboard, a teacher desk and some desks inside'''

	#x,y,z of a single desk
	deskX = 1.2
	deskY = 0.7
	deskZ = 0.9
	
	#desks distances
	wallDist = 1.0
	deskDist = 0.5

	#x,y,z of the blackboard
	blackboardX = 6
	blackboardY = 2
	blackboardZ = 0.1

	#x,y,z of the teacher desk
	teachDeskX = 1.5
	teachDeskY = 1.0
	teachDeskZ = 1.0

	#creates a single desk with two chairs
	deskChair = ggpl_desk_chair(deskX,deskY,deskZ)
	#insert the first desk and chairs inside the first row of the classroom
	row = T(1)(wallDist)(deskChair)
	#the counter is initialized at distance from the wall + length ad a desk + distance between desks
	count = deskX + deskDist + wallDist
	while dx - deskDist > count + deskX :
		row = STRUCT([row,T(1)(count),deskChair])
		count += deskDist + deskX

	#insert the first row inside the classroom
	room = T(2)(wallDist)(row)
	count2 = deskDist + deskY + wallDist
	while dy - deskDist > (count2 + deskY) *1.5 :
		room = STRUCT([room,T(2)(count2),row])
		count2 += deskDist + deskY

	#creates the blackboard
	blackboard = ggpl_blackboard(blackboardX,blackboardY,blackboardZ)
	blackboard = R([2,3])(PI/2)(blackboard)
	blackboard = T(1)((dx/2) - (blackboardX/2))(blackboard)
	blackboard = T(2)(dy)(blackboard)
	blackboard = T(3)(dz/4)(blackboard)
	room = STRUCT([room,blackboard])

	#creates the teacher desk
	teachDesk = ggpl_teacher_desk_chair(teachDeskX,teachDeskY,teachDeskZ)
	teachDesk = R([1,2])(PI)(teachDesk)
	teachDesk = T(1)((dx/2) + (teachDeskX/2))(teachDesk)
	teachDesk = T(2)(dy - wallDist*1.5)(teachDesk)
	room = STRUCT([room,teachDesk])

	#creates a box aroud the class
	box = SKEL_1(CUBOID([dx,dy,dz]))

	VIEW(STRUCT([room,box]))

def main():
	#VIEW(ggpl_blackboard(6,2,.1))
	#VIEW(ggpl_desk(1.2,0.7,0.9))
	#VIEW(ggpl_chair(0.5,0.6,1.2))
	#VIEW(ggpl_desk_chair(1.2,0.7,0.9))
	#VIEW(ggpl_teacher_desk_chair(1.5,1,1))
	ggpl_classroom(12,10,3.5)

if __name__ == '__main__':
	main()
