"""workshop_11.py
Creates a model of the suburban neighborhood found at this link:
https://github.com/VAle512/ggpl/blob/master/2017-01-27/jupyter_images/workshop_11_model.jpg
"""

from pyplasm import *
import csv
from lib import workshop_10 as w_10


def neighborhoodAssembler(streets, house):
	'''Put several houses in the right location.
	@param streets: the streets system where the houses have to be located
	@param house: the model of the house
	@return nb: the model of a neighborhood with streets and houses
	'''

	streets = S([1,2,3])([1.5,1.5,1.5])(streets)
	house = S([1,2,3])([.9,.9,.9])(house)

	house1 = R([1,2])(3*PI/2)(house)
	house1 = T([1,2])([40,50])(house1)
	nb = STRUCT([streets,house1])
	house1 = T([2])([30])(house1)
	nb = STRUCT([nb,house1])
	house1 = T([2])([30])(house1)
	nb = STRUCT([nb,house1])
	house1 = T([2])([30])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(PI)(house)
	house1 = T([1,2])([85,100])(house1)
	nb = STRUCT([nb,house1])
	house1 = T([1])([25])(house1)
	nb = STRUCT([nb,house1])
	house1 = T([1])([25])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(3*PI/2)(house)
	house1 = T([1,2])([190,20])(house1)
	nb = STRUCT([nb,house1])
	house1 = T([2])([25])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(-3*PI/8)(house)
	house1 = T([1,2])([180,80])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(PI/2)(house)
	house1 = T([1])([235])(house1)
	nb = STRUCT([nb,house1])
	house1 = T([2])([25])(house1)
	nb = STRUCT([nb,house1])
	house1 = T([2])([25])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(3*PI/4)(house)
	house1 = T([1,2])([238,90])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(PI)(house)
	house1 = T([1,2])([180,115])(house1)
	nb = STRUCT([nb,house1])
	house1 = T([1])([25])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(3*PI/4)(house)
	house1 = T([1,2])([135,65])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(PI)(house)
	house1 = T([1,2])([150,65])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(7*PI/4)(house)
	house1 = T([1,2])([90,45])(house1)
	nb = STRUCT([nb,house1])
	house1 = T([1,2])([120,20])(house)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(PI)(house)
	house1 = T([1,2])([22,175])(house1)
	nb = STRUCT([nb,house1])
	house1 = T([1])([25])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(5*PI/4)(house)
	house1 = T([1,2])([57,184])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(5*PI/4)(house)
	house1 = T([1,2])([75,200])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(5*PI/4)(house)
	house1 = T([1,2])([97,215])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(PI)(house)
	house1 = T([1,2])([130,215])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(PI)(house)
	house1 = T([1,2])([155,220])(house1)
	nb = STRUCT([nb,house1])
	house1 = T([1])([25])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(PI)(house)
	house1 = T([1,2])([210,210])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(3*PI/4)(house)
	house1 = T([1,2])([240,187])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(3*PI/4)(house)
	house1 = T([1,2])([260,170])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(3*PI/4)(house)
	house1 = T([1,2])([280,150])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(3*PI/4)(house)
	house1 = T([1,2])([300,130])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(3*PI/4)(house)
	house1 = T([1,2])([320,110])(house1)
	nb = STRUCT([nb,house1])
	house1 = R([1,2])(PI/2)(house)
	house1 = T([1])([355])(house1)
	nb = STRUCT([nb,house1])
	house1 = T([2])([30])(house1)
	nb = STRUCT([nb,house1])
	house1 = T([2])([30])(house1)
	nb = STRUCT([nb,house1])

	return nb

def treeAssembler(nb,tree):
	'''Put several trees in the right location.
	@param nb: the neighborhood where trees have to be located
	@param tree: the model of a tree
	@return nb: the model of a neighborhood with trees in it
	'''

	#top left trees
	nb = STRUCT([(T([1])([70])(tree)),nb])
	nb = STRUCT([(T([1,2])([70,10])(tree)),nb])
	nb = STRUCT([(T([1,2])([70,20])(tree)),nb])
	nb = STRUCT([(T([1,2])([70,30])(tree)),nb])

	#far right trees
	nb = STRUCT([(T([1,2])([70,110])(tree)),nb])
	nb = STRUCT([(T([1,2])([70,120])(tree)),nb])
	nb = STRUCT([(T([1,2])([70,130])(tree)),nb])
	nb = STRUCT([(T([1,2])([70,140])(tree)),nb])
	nb = STRUCT([(T([1,2])([70,150])(tree)),nb])
	nb = STRUCT([(T([1,2])([80,160])(tree)),nb])
	nb = STRUCT([(T([1,2])([90,170])(tree)),nb])
	nb = STRUCT([(T([1,2])([100,175])(tree)),nb])
	nb = STRUCT([(T([1,2])([110,180])(tree)),nb])
	nb = STRUCT([(T([1,2])([120,185])(tree)),nb])
	nb = STRUCT([(T([1,2])([130,190])(tree)),nb])
	nb = STRUCT([(T([1,2])([145,180])(tree)),nb])
	nb = STRUCT([(T([1,2])([145,170])(tree)),nb])
	nb = STRUCT([(T([1,2])([145,190])(tree)),nb])
	nb = STRUCT([(T([1,2])([160,190])(tree)),nb])
	nb = STRUCT([(T([1,2])([160,180])(tree)),nb])
	nb = STRUCT([(T([1,2])([160,170])(tree)),nb])
	nb = STRUCT([(T([1,2])([170,185])(tree)),nb])
	nb = STRUCT([(T([1,2])([180,183])(tree)),nb])
	nb = STRUCT([(T([1,2])([190,180])(tree)),nb])
	nb = STRUCT([(T([1,2])([200,178])(tree)),nb])
	nb = STRUCT([(T([1,2])([210,170])(tree)),nb])
	nb = STRUCT([(T([1,2])([220,165])(tree)),nb])
	nb = STRUCT([(T([1,2])([230,157])(tree)),nb])
	nb = STRUCT([(T([1,2])([240,150])(tree)),nb])
	nb = STRUCT([(T([1,2])([250,140])(tree)),nb])
	nb = STRUCT([(T([1,2])([260,125])(tree)),nb])
	nb = STRUCT([(T([1,2])([265,115])(tree)),nb])

	#bottom left park
	nb = STRUCT([(T([1,2])([280,2])(tree)),nb])
	nb = STRUCT([(T([1,2])([280,10])(tree)),nb])
	nb = STRUCT([(T([1,2])([280,20])(tree)),nb])
	nb = STRUCT([(T([1,2])([280,30])(tree)),nb])
	nb = STRUCT([(T([1,2])([280,40])(tree)),nb])
	nb = STRUCT([(T([1,2])([280,50])(tree)),nb])
	nb = STRUCT([(T([1,2])([280,60])(tree)),nb])
	nb = STRUCT([(T([1,2])([280,70])(tree)),nb])
	nb = STRUCT([(T([1,2])([280,80])(tree)),nb])
	nb = STRUCT([(T([1,2])([280,90])(tree)),nb])
	nb = STRUCT([(T([1,2])([280,100])(tree)),nb])
	nb = STRUCT([(T([1,2])([290,92])(tree)),nb])
	nb = STRUCT([(T([1,2])([300,87])(tree)),nb])
	nb = STRUCT([(T([1,2])([310,83])(tree)),nb])
	nb = STRUCT([(T([1,2])([318,78])(tree)),nb])
	nb = STRUCT([(T([1,2])([325,75])(tree)),nb])
	nb = STRUCT([(T([1,2])([325,65])(tree)),nb])
	nb = STRUCT([(T([1,2])([325,55])(tree)),nb])
	nb = STRUCT([(T([1,2])([325,45])(tree)),nb])
	nb = STRUCT([(T([1,2])([325,35])(tree)),nb])
	nb = STRUCT([(T([1,2])([325,25])(tree)),nb])
	nb = STRUCT([(T([1,2])([325,15])(tree)),nb])
	nb = STRUCT([(T([1,2])([325,2])(tree)),nb])

	return nb

def treeBuilder(h):
	'''Create a tree with the given height.
	@param h: the height of the tree
	@return nb: the tree created
	'''

	r = h/15.
	log = CYLINDER([r,h])(64)
	log = MATERIAL([.05,.05,.05,1, .4,.2,0,1, 0,0,0,0, 0,0,0,1, 100])(log)
	foliage = SPHERE(h/4.)([64,64])
	foliage = MATERIAL([.05,.05,.05,1, .33,1,.07,1, 0,0,0,0, 0,0,0,1, 100])(foliage)
	foliage = T(3)(h)(foliage)
	tree = STRUCT([log,foliage])
	return tree

def streetsBuilder(lines):
	'''Creates a streets system from a collection of points
	@param lines: a collection of points representing the streets
	@return st: a model of the streets system created 
	'''

	st = STRUCT([CUBOID([0,0,0])])
	st = DIFFERENCE([st,st])
	for el in lines:
		strada = MAP(BEZIER(S1)(el))(INTERVALS(1)(32))
		st = STRUCT([strada,st])
	st = OFFSET([4,4,1])(st)
	st = MATERIAL([.05,.05,.05,1, .25,.25,.25,1, 0,0,0,0, 0,0,0,1, 100])(st)
	return st

def createPlattfrom(nb):
	'''Creates a plattform for the given neighborhood model
	@param nb: the neighborhood model to put on top of the plattform
	@return plattform: the plattform for the neighborhood model, without the model on top
	'''

	boxTop =  SKEL_1(BOX([1,2])(nb))
	boxTop = SOLIDIFY(boxTop)
	box = OFFSET([1,1,9])(boxTop)
	box = T([3])([-12])(box)
	box = MATERIAL([.05,.05,.05,1, .4,.2,0,1, 0,0,0,0, 0,0,0,1, 100])(box)
	boxTop = OFFSET([1,1,2])(boxTop)
	boxTop = T([3])([-3])(boxTop)
	boxTop = TEXTURE('textures/workshop_11_erba.jpeg')(boxTop)
	plattform = STRUCT([box,boxTop])
	return plattform

def ggpl_suburban_neighborhood_builder(streetsPoints):
	'''Creates a neighborhood model, starting from a collection of point
	@param streetsPoints: the collection of points representing the streets system of the model
	@return nb: the neighborhood model created with streets, houses and trees, on top of a plattform
	'''

	streets = streetsBuilder(streetsPoints)
	house = w_10.ggpl_house_builder()
	nb = neighborhoodAssembler(streets, house)
	tree = treeBuilder(5)
	nb = treeAssembler(nb,tree)
	plattform = createPlattfrom(nb)
	nb = STRUCT([nb,plattform])

	return nb

def main():

	streetsPoints = [[[40,0],[40,100]],[[0,100],[40,100]],[[40,50],[100,50]],[[100,0],[100,130]],[[100,60],[120,60]],[[140,0],[140,50]],[[180,0],[180,80]],[[220,0],[220,50]],[[40,100],[70,130],[80,126],[100,130]],[[100,130],[120,126],[150,120],[180,80]],[[180,80],[184,70],[220,50]],[[64,50],[74,24],[100,24]],[[120,60],[140,58],[140,50]]]
	VIEW(ggpl_suburban_neighborhood_builder(streetsPoints))

if __name__ == '__main__':
	main()
