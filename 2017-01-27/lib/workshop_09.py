"""workshop_09
build a roof starting from a .lines file rappresenting the vertices of the roof's base

"""

import csv
import math
from itertools import *
from larlib import *

def makeUnique(original_list):

    uniqueList = []
    [uniqueList.append(obj) for obj in original_list if obj not in uniqueList]
    return uniqueList

def polygonArea(x, y):
    '''Calculates the area of polygon given its vertices'''
    area = 0.0
    for i in xrange(-1, len(x) - 1):
        area += x[i] * (y[i + 1] - y[i - 1])
    return area / 2.0

def polygonCentroid(points):
	'''Calculates the centroid of polygon given its vertices'''
	area = polygonArea(*zip(*points))
	resultX = 0
	resultY = 0
	N = len(points)
	points = cycle(points)
	x1, y1 = next(points)
	for i in range(N):
		x0, y0 = x1, y1
		x1, y1 = next(points)
		cross = (x0 * y1) - (x1 * y0)
		resultX += (x0 + x1) * cross
		resultY += (y0 + y1) * cross
	resultX /= (area * 6.0)
	resultY /= (area * 6.0)
	return (resultX, resultY)

def orderClockwise(points):

	firstPoint = points[0]
	centroid = [firstPoint[0],firstPoint[1]+0.0000001]
	print centroid
	firstLength = distance(centroid,firstPoint)
	newPoints = []

	while len(points)>0:
		cos = 400
		for j in range(len(points)):
			cos2 = findAngle(points[j],centroid)
			
			if cos2 < cos:
				cos = cos2
				p = points[j]
		newPoints.append(p)
		for t in range(len(points)):
			if points[t] == p:
				el = t
		
		points.pop(el)
		
	return newPoints 

def distance(p1,p2):
	'''return the distance between two given points'''
	return float(math.sqrt(math.pow((p1[0] - p2[0]), 2)+math.pow((p1[1] - p2[1]), 2)))

def findAngle(p1,p2):

	return math.atan2(p1[1]-p2[1],p1[0]-p2[0])

def ggpl_roof_builder(externalWallsLinesPath):
	'''build a roof starting from a .lines file rappresenting the vertices of the roof's base
	@param: the name of the .lines file. It must be located in the lines folder
	@rerturn: the HPC value of the roof'''
	j=0
	s=0
	t=0
	firstShape = []
	falde = []
	topShape = []
	pol= []
	pol2 = []
	with open(externalWallsLinesPath, "rb") as file:
		reader = csv.reader(file, delimiter=",")
		polylineList = []
		reader2 = reader
		row1=next(reader2)
		px = row1[0]
		py = row1[1]
	with open(externalWallsLinesPath, "rb") as file:
		reader = csv.reader(file, delimiter=",")
		for row in reader:
			firstShape.append([float(row[0])-float(px),float(row[1])-float(py)])
			firstShape.append([float(row[2])-float(px),float(row[3])-float(py)])
	centroid = polygonCentroid(firstShape)
	[x,y] = centroid
	centroid = [x,y]

	for f in range(len(firstShape)):
		firstShape[f][0]=firstShape[f][0]-centroid[0]
		firstShape[f][1]=firstShape[f][1]-centroid[1]
	while j<len(firstShape):
		pol.append(POLYLINE([firstShape[j],firstShape[j+1]]))
		j=j+2
	pol = STRUCT(pol)

	for i in range(len(firstShape)):
		topShape.append([firstShape[i][0]/2.0,firstShape[i][1]/2.0])

	firstShape = makeUnique(firstShape)

	topShape = makeUnique(topShape)
	topShape= orderClockwise(topShape)
	firstShape = orderClockwise(firstShape)
	topShape = topShape + [topShape[0]]
	while t<len(topShape)-1:
		pol2.append(POLYLINE([topShape[t],topShape[t+1]]))
		t=t+1

	piano = SOLIDIFY(STRUCT(pol2))
	piano = T(3)(4)(piano)
	firstShape = firstShape+ [firstShape[0]]
	for p in range(len(firstShape)):
		firstShape[p]=firstShape[p]+[float(0)]
	for k in range(len(topShape)):
		topShape[k]=topShape[k]+[float(4)]

	while s<len(makeUnique(firstShape)):
		falde.append(MKPOL([[firstShape[s],firstShape[s+1],topShape[s],topShape[s+1]],[[1,2,3,4]],None]))
		s = s+1
	falde = STRUCT(falde)
	roof = STRUCT([falde,piano])
	roof = T([1,2])([centroid[0],centroid[1]])(roof)
	return roof

def main():
	VIEW(ggpl_roof_builder("workshop_09_linee_tetto"))


if __name__ == '__main__':
	main()
