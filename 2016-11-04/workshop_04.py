"""workshop_04.py

Exract informations from the HPC value of two given roof, creating a copy of them with highlighted beams.
"""

from larlib import *
from ast import literal_eval

def hpc_builder(verts,cells):
	'''returns the HPC value of a roof created with the parameters given
	@param verts: List that contain all verts.
	@param cells: List that contain all cells.'''

	struct = MKPOL([verts, cells,None])
	return struct

def verts_rounder(verts):
	'''round all the values given in input to the 2nd decimal
	@param verts: List of values to round.'''

	vertsR = []
	for i in range(len(verts)):
		listTemp = verts[i]
		for j in range(len(listTemp)):
			listTemp[j] = round(listTemp[j],2)
		vertsR.append(listTemp)
	return vertsR


def create_dict(verts,cells):
	'''creates a dictionary containing the cells and using verts as key
	@param verts: List that contain all verts.
	@param cells: List that contain all cells.'''

	dct={}
	dictKey=[]
	
	i=1
	for v in verts:
		#string type keys
		key=",".join(str(x) for x in v)
		if not key in dct.keys():
			dct[key]=[i]
		else: 
			dct.get(key).append(i)
		i+=1

	for key in dct.keys():
		dictKey.append(literal_eval(key))

	return (dct,dictKey)

def ggpl_roof_builder(roof):
	'''extract verts and cells lists from the given HPC value of a roof and creates a new roof with highlighted beams
	@param roof: HPC value of a roof.'''

	#extract verts and cells values from the HPC
	(verts,cells,n) = UKPOL(SKEL_2(roof))
	#rounds all values in verts
	vertsR = verts_rounder(verts)
	#creates the dictionary
	(dictionary,dictionaryKey) = create_dict(verts,cells)
	#creates the new roof
	newRoof = MKPOL([vertsR,cells,None])
	#extract the beams of the new roof
	beams = OFFSET([.1,.1,.1])(SKEL_1(newRoof))
	#paint the beams in black
	beamsB = COLOR(BLACK)(beams)

	VIEW(STRUCT([newRoof,beamsB]))

def main():

	#Gabled roof
	verts = [[0,0,0],[6,0,0],[0,7,0],[6,7,0],[3,0,3],[3,7,3]]
	cells = [[1,2,5],[1,3,5,6],[3,4,6],[2,4,5,6]]
	hpc = hpc_builder(verts,cells)
	ggpl_roof_builder(hpc)

	#Gambrel roof
	verts2=[[0,0,0],[4,0,5],[4,24,5],[0,24,0],[12,0,8],[12,24,8],[20,0,5],[20,24,5],[24,0,0],[24,24,0]]
	cells2=[[1,2,3,4],[2,3,6,5],[5,6,8,7],[7,8,10,9],[1,2,5,7,9],[3,4,6,8,10]]
	hpc2 = hpc_builder(verts2,cells2)
	ggpl_roof_builder(hpc2)

if __name__ == '__main__':
	main()
