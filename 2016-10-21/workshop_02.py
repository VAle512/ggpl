from larlib import * 

import csv

"""read data from a csv file"""
def readCSV(file_name):
	
	frameDist = []
	with open(file_name, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		i=0
		for row in reader:
			if i%2==1:
				frameDist.append(float(row[0]))
				i=i+1
			elif i%2==0:
				(px,py)=(float(row[0]),float(row[1]))
				pillarsDist = []
				j=3
				while row[j]!="]":
					pillarsDist.append(float(row[j]))
					j=j+1
				(by,bz)= (float(row[j+1]),float(row[j+2]))
				j= j+4
				beamsDist = []
				while row[j]!="]":
					beamsDist.append(float(row[j]))
					j=j+1	
				i=i+1
		csvfile.close()

	return (px,py, pillarsDist, by,bz, beamsDist, frameDist)

"""return a 3D value of type HPC of the structure with the given parameters"""
def buildStruct(px,py,pillarsDist,by,bz, beamsDist, frameDist):

	#the following code creates a single frame
	pillarArray = [px]
	for value in pillarsDist:
		pillarArray = pillarArray+[-value]+[px]
	xPillar = QUOTE(pillarArray)
	yPillar = QUOTE([py])
	xyPillar = PROD([xPillar, yPillar])
	heightsPillar = []
	for value in beamsDist:
		heightsPillar.append((value+bz))
	zPillar = QUOTE(heightsPillar)
	pillars = PROD([xyPillar, zPillar])
	beamArray = []
	for value in pillarArray:
		beamArray.append(-value)
	xBeam = QUOTE(beamArray)
	yBeam = QUOTE([by])
	xyBeam = PROD([xBeam, yBeam])
	beamsArrayDist = []
	for value in beamsDist:
		beamsArrayDist.append(-value)
		beamsArrayDist.append(bz)
	beams = PROD([xyBeam, QUOTE(beamsArrayDist)])
	#the single frame created
	frame = STRUCT([pillars, beams])

	#the following code duplicates the frames and creates the beams between each frame
	framesArrayDist = []
	for value in frameDist:
		framesArrayDist.append(-py)
		framesArrayDist.append(value)
	yFrameBeams = QUOTE(framesArrayDist)
	xyFrameBeams = PROD([yBeam, yFrameBeams])
	xyzFrameBeams = PROD([xyFrameBeams, QUOTE(beamsArrayDist)])
	xyzFrame = STRUCT([xyzFrameBeams])
	
	accB = 0
	arrayBeams = []
	for value in frameDist:
		accB+=value
		arrayBeams.append(accB)
	distB=py
	structFrames=frame
	for value in arrayBeams:
		structFrames = STRUCT([structFrames, T(2)(value+distB), frame])
		distB+=py

	accP = 0
	arrayPillar = []
	for value in pillarsDist:
		accP+=value
		arrayPillar.append(accP)
	distP=px
	structBeams= xyzFrame
	for value in arrayPillar:
		structBeams = STRUCT([structBeams, T(1)(value+distP), xyzFrame])
		distP+=px

	#merge frame and beams to create the final structure
	finalStruct =  STRUCT([structFrames, structBeams])

	return finalStruct

"""visualize a type HPC of a 3D structure. The data to build the structure are in a csv file given in input"""
def ggpl_bone_structure(csvFileName):

	#read data from the csv file and save them in structureData
	structureData = readCSV(csvFileName)
	
	#extract eache single parameter for buildStruct from structureData
	px = structureData[0]
	py = structureData[1]
	pillarDist = structureData[2]
	by = structureData[3]
	bz = structureData[4]
	beamDist = structureData[5]
	frameDist = structureData[6]

	#create the structure
	struct = buildStruct(px,py,pillarDist,by,bz,beamDist,frameDist)
	
	#visualize the structure
	VIEW(struct)

def main():
	ggpl_bone_structure('frame_data_457856.csv')

if __name__=='__main__':
	main()