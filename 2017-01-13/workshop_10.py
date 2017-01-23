"""workshop_10.py
Creates a 3D model of an house
"""

from larlib import *

from res import workshop_08 as w_08

def ggpl_house_builder():

	#.lines paths
	externalWallsLinesPath = "lines/workshop_10_muri_esterni.lines"
	internalWallsLinesPath = "lines/workshop_10_muri_interni.lines"
	windowsLinesPath = "lines/workshop_10_finestre.lines"
	internalDoorsLinesPath = "lines/workshop_10_porte.lines"
	externalDoorsLinesPath = "lines/workshop_10_porte_esterne.lines"

	#window parameters
	XWindow = [.05,1,.05,1,.05,1,.05]
	YWindow = [.05,1.2,.1,.7,.05]
	occurencesWindow = [[1,1,1,1,1,1,1],[1,0,1,0,1,0,1],[1,1,1,1,1,1,1],[1,0,1,0,1,0,1],[1,1,1,1,1,1,1]]

	#door parameters
	XDoor = [.06,.07,.12,.09,.06]
	YDoor = [.2,.2,.2,.2,.2,.2,.2]
	occurencesDoor = [[1,1,1,1,1],[1,1,0,0,1],[1,1,1,1,1],[1,0,0,1,1],[1,1,1,1,1],[1,1,0,0,1],[1,1,1,1,1]]
	
	VIEW(w_08.ggpl_house_builder(externalWallsLinesPath,internalWallsLinesPath,windowsLinesPath,internalDoorsLinesPath,externalDoorsLinesPath)(XWindow,YWindow,occurencesWindow)(XDoor,YDoor,occurencesDoor))

def main():
	ggpl_house_builder()

if __name__ == '__main__':
	main()
