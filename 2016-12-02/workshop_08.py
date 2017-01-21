"""workshop_08.py
creates the 3D map of an house starting from several lines files

"""

import csv
from pyplasm import *

####### LINES FILE PATHS #######
externalWallsLinesPath = "lines/workshop_08_muri_esterni.lines"
internalWallsLinesPath = "lines/workshop_08_muri_interni.lines"
windowsLinesPath = "lines/workshop_08_finestre.lines"
internalDoorsLinesPath = "lines/workshop_08_porte.lines"
externalDoorsLinesPath = "lines/workshop_08_porte_esterne.lines"


def ggpl_house_builder():
	'''creates the 3D map of an house starting from several lines files
	@return the HPC value of the map
	'''

	####### EXTERNAL WALLS SECTION #######

	with open(externalWallsLinesPath, "rb") as csvfile:
		csvReader = csv.reader(csvfile,delimiter=",")
		externalWalls_list = []
		for row in csvReader :
			externalWalls_list.append(POLYLINE([[float(row[0]),float(row[1])],[float(row[2]),float(row[3])]]))
	externalWalls = STRUCT(externalWalls_list)
	xScale = 16/SIZE([1])(externalWalls)[0]
	yScale = 16/SIZE([2])(externalWalls)[0]
	externalWalls = S([1,2])([xScale,yScale])(externalWalls)
	
	pavement = SOLIDIFY (externalWalls)
	pavement = TEXTURE("textures/workshop_08_texture_pavimento.jpeg")(pavement)
	
	externalWalls = OFFSET([.15,.15])(externalWalls)
	externalWalls = PROD([externalWalls,Q(3.5)])


	####### INTERNAL WALLS SECTION #######

	with open(internalWallsLinesPath, "rb") as csvfile:
		csvReader = csv.reader(csvfile,delimiter=",")
		internalWalls_list = []
		for row in csvReader :
			internalWalls_list.append(POLYLINE([[float(row[0]),float(row[1])],[float(row[2]),float(row[3])]]))
	internalWalls = STRUCT(internalWalls_list)
	internalWalls = S([1,2])([xScale,yScale])(internalWalls)
	internalWalls = OFFSET([.1,.1])(internalWalls)
	internalWalls = PROD([internalWalls,Q(3)])
	

	####### WINDOWS SECTION #######	
	
	with open(windowsLinesPath, "rb") as csvfile:
		csvReader = csv.reader(csvfile,delimiter=",")
		listWindowsHoles = []
		listWindowsCreated = []
		cuboid = []
		cont = 0
		for row in csvReader:
			cont += 1
			cuboid.append([float(row[0])*xScale,float(row[1])*yScale])
			if cont == 4:
				listWindowsHoles.append(MKPOL([cuboid,[[1,2,3,4]],None]))
				base = MKPOL([cuboid,[[1,2,3,4]],None])
				#base = OFFSET([.1,.1])(base)
				base = PROD([base,Q(1.5)])
				cuboid = []
				cont = 0

	windows = STRUCT(listWindowsHoles)
	windows = OFFSET([0.2,0.2])(windows)
	windows = PROD([windows,Q(1.5)])
	windows = T(3)(1)(windows)


	####### DOORS SECTION #######

	with open(internalDoorsLinesPath, "rb") as csvfile:

		csvReader = csv.reader(csvfile,delimiter=",")
		listInternalDoorsHoles = []
		cuboid = []
		initHoles = True
		cont = 0
		xDoors = 0
		yDiff = 0
		listInternalDoorsCreated = []
		for row in csvReader:
			cont += 1
			cuboid.append([float(row[0])*xScale,float(row[1])*yScale])
			if cont == 4:
				listInternalDoorsHoles.append(MKPOL([cuboid,[[1,2,3,4]],None]))
				cuboid = []
				door = []
				cont = 0

	internalDoorsHoles = STRUCT(listInternalDoorsHoles)
	internalDoorsHoles = OFFSET([.2,.15])(internalDoorsHoles)
	internalDoorsHoles = PROD([internalDoorsHoles,Q(3)])

	with open(externalDoorsLinesPath,"rb") as csvfile:
		csvReader = csv.reader(csvfile, delimiter=",")
		listExternalDoorsHoles = []
		cuboid = []
		initHoles = True
		cont = 0
		xDiff = 0
		yDiff = 0
		listExternalDoorsCreated = []
		for row in csvReader:
			cont += 1
			cuboid.append([float(row[0]) * xScale, float(row[1]) * yScale])
			if cont == 4:
				listExternalDoorsHoles.append(MKPOL([cuboid, [[1, 2, 3, 4]], None]))
				cuboid = []
				door = []
				cont = 0

	externalDoorsHoles = STRUCT(listExternalDoorsHoles)
	externalDoorsHoles = OFFSET([0,.15])(externalDoorsHoles)
	externalDoorsHoles = PROD([externalDoorsHoles,Q(2.5)])


	####### FINAL BUILDING SECTION #######

	externalWalls = DIFFERENCE([externalWalls,windows])
	externalWalls = DIFFERENCE([externalWalls,externalDoorsHoles])
	externalWalls = TEXTURE("textures/workshop_08_texture_muro_esterno.jpeg")(externalWalls)
	internalWalls = DIFFERENCE([internalWalls,internalDoorsHoles])
	internalWalls = TEXTURE("textures/workshop_08_texture_muro_interno.jpg")(internalWalls)
	walls = STRUCT([internalWalls,externalWalls])
	house = STRUCT([walls,pavement])

	return house

def main():
	VIEW(ggpl_house_builder())


if __name__ == '__main__':
	main()
