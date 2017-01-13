"""workshop_09


"""

from pyplasm import *
import csv

def generate_2D_walls(fileName):
	with open("lines/" + fileName +  ".lines", "rb") as file:
		reader = csv.reader(file, delimiter=",")
		polygonLines = []
		for line in reader:
			polygonLines.append(POLYLINE([[float(line[0]), float(line[1])],[float(line[2]), float(line[3])]]))
	struct = STRUCT(polygonLines)
	xScale = 8/SIZE([1])(struct)[0]
	yScale = 8/SIZE([2])(struct)[0]
	structS = S([1,2])([xScale,yScale])(struct)
	return structS

def ggpl_roof_builder():
	lines = generate_2D_walls("tetto")
	VIEW(lines)

def main():
	ggpl_roof_builder()

if __name__=='__main__':
	main()
