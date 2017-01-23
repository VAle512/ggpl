"""workshop_08.py

"""

import csv
from pyplasm import *
from res import workshop_03 as w_03
from res import workshop_07 as w_07
from res import workshop_09 as w_09

def ggpl_house_builder(externalWallsLinesPath,internalWallsLinesPath,windowsLinesPath,internalDoorsLinesPath,externalDoorsLinesPath):

	def ggpl_house_builder_aux0(XWindow,YWindow,occurencesWindow):

		def ggpl_house_builder_aux1(XDoor,YDoor,occurencesDoor):

			####### EXTERNAL WALLS AND ROOF SECTION #######

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
			pavement = TEXTURE("textures/workshop_10_texture_pavimento.jpeg")(pavement)
			
			externalWalls = OFFSET([.2,.2])(externalWalls)
			externalWalls = PROD([externalWalls,Q(3.5)])

			roof = w_09.ggpl_roof_builder(externalWallsLinesPath)
			roof = T([1,2])([float(row[0]),float(row[1])])(roof)
			roof = S([1,2])([xScale,yScale])(roof)
			roof = TEXTURE("textures/workshop_10_tetto.jpg")(roof)


			####### INTERNAL WALLS SECTION #######

			with open(internalWallsLinesPath, "rb") as csvfile:
				csvReader = csv.reader(csvfile,delimiter=",")
				internalWalls_list = []
				for row in csvReader :
					internalWalls_list.append(POLYLINE([[float(row[0]),float(row[1])],[float(row[2]),float(row[3])]]))
			internalWalls = STRUCT(internalWalls_list)
			internalWalls = S([1,2])([xScale,yScale])(internalWalls)
			internalWalls = OFFSET([.2,.2])(internalWalls)
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
					if cont <=2:
						if 	round(float(row[0]),1) == round(float(row[2]),1):
							yDiff = abs(float(row[3]) - float(row[1]))
						elif round(float(row[1]),1) == round(float(row[3]),1):
							xDiff = abs(float(row[2]) - float(row[0]))
					if cont == 4:
						listWindowsHoles.append(MKPOL([cuboid,[[1,2,3,4]],None]))
						base = MKPOL([cuboid,[[1,2,3,4]],None])
						base = OFFSET([.1,.1])(base)
						base = PROD([base,Q(1.5)])
						cuboid = []
						cont = 0
						if xDiff < yDiff:
							window = w_07.ggpl_window(XWindow,YWindow,occurencesWindow)(yDiff*yScale,1.5,1.5)
							window = R([1,2])(3*PI/2)(window)
						else:
							window = w_07.ggpl_window(XWindow,YWindow,occurencesWindow)(xDiff*xScale +.2,1.5,1.5)
						
						window = T([1,2,3])([float(row[0])*xScale, float(row[1])*yScale,1])(window)
						listWindowsCreated.append(window)

			windows = STRUCT(listWindowsHoles)
			windows = OFFSET([0.05,0.05])(windows)
			windows = PROD([windows,Q(1.5)])
			windows = T(3)(1)(windows)
			windowsCreated = STRUCT(listWindowsCreated)


			####### DOORS AND STAIR SECTION #######

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
					if cont <=2:
						if 	round(float(row[0]),1) == round(float(row[2]),1):
							yDiff = abs(float(row[3]) - float(row[1]))
						
						elif round(float(row[1]),1) == round(float(row[3]),1):
							xDiff = abs(float(row[2]) - float(row[0]))

					if cont == 4:
						listInternalDoorsHoles.append(MKPOL([cuboid,[[1,2,3,4]],None]))
						cuboid = []
						door = []
						cont = 0
						if xDiff < yDiff:
							door = w_07.ggpl_door(XDoor,YDoor,occurencesDoor)(yDiff*yScale,3,.1)
							door = T([2])([.4])(door)
							door = R([1,2])(3*PI/2)(door)
						else:
							door = w_07.ggpl_door(XDoor,YDoor,occurencesDoor)(xDiff*xScale,3,.1)

						door = T([1,2])([float(row[0])*xScale,float(row[1])*yScale])(door)
						listInternalDoorsCreated.append(door)

			internalDoorsHoles = STRUCT(listInternalDoorsHoles)
			internalDoorsHoles = OFFSET([.2,.15])(internalDoorsHoles)
			internalDoorsHoles = PROD([internalDoorsHoles,Q(3)])
			internalDoorsCreated = STRUCT(listInternalDoorsCreated)

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
					if cont <= 2:
						if round(float(row[0]), 1) == round(float(row[2]), 1):
							yDiff = abs(float(row[3]) - float(row[1]))
						elif round(float(row[1]), 1) == round(float(row[3]), 1):
							xDiff = abs(float(row[2]) - float(row[0]))

					if cont == 4:
						listExternalDoorsHoles.append(MKPOL([cuboid, [[1, 2, 3, 4]], None]))
						cuboid = []
						door = []
						cont = 0
						if xDiff < yDiff:
							door = w_07.ggpl_door(XDoor, YDoor, occurencesDoor)(yDiff * yScale, 2.5,.1)
							door = R([1, 2])(PI/2)(door)
						else:
							door = w_07.ggpl_door(XDoor, YDoor, occurencesDoor)(xDiff * xScale, 2.5,.1)

						door = T([1, 2])([float(row[0]) * xScale, float(row[1]) * yScale])(door)
						listExternalDoorsCreated.append(door)

				stair = w_03.ggpl_single_stair(8.,6.,3.5)
				stair = R([1,2])(PI)(stair)
				stair = T([1,2])([float(row[0]) * xScale+2.5, float(row[1]) * yScale+6])(stair)
				stair = TEXTURE("textures/workshop_10_scale.jpg")(stair)

			externalDoorsHoles = STRUCT(listExternalDoorsHoles)
			externalDoorsHoles = OFFSET([0,.15])(externalDoorsHoles)
			externalDoorsHoles = PROD([externalDoorsHoles,Q(2.5)])
			externalDoorsCreated = STRUCT(listExternalDoorsCreated)	


			####### FINAL BUILDING SECTION #######

			externalWalls = DIFFERENCE([externalWalls,windows])
			externalWalls = DIFFERENCE([externalWalls,externalDoorsHoles])
			externalWalls = TEXTURE("textures/workshop_10_texture_muro_esterno.jpeg")(externalWalls)
			externalWalls = STRUCT([externalWalls,windowsCreated])
			externalWalls = STRUCT([externalWalls, externalDoorsCreated])

			internalWalls = DIFFERENCE([internalWalls,internalDoorsHoles])
			internalWalls = TEXTURE("textures/workshop_10_texture_muro_interno.jpg")(internalWalls)
			internalWalls = STRUCT([internalWalls,internalDoorsCreated])

			walls = STRUCT([internalWalls,externalWalls])

			house = STRUCT([walls,pavement])
			house = STRUCT([house,T(3)(3.5),house])
			house = STRUCT([house,stair])

			VIEW(house) #the house with no roof

			house = STRUCT([house,T(3)(7),roof])

			return house

		return ggpl_house_builder_aux1

	return ggpl_house_builder_aux0

def main():
	VIEW(ggpl_house_builder())


if __name__ == '__main__':
	main()
