from larlib import *

def buildStruct(px,py,pillarsDist,by,bz,beamsDist):
	"""create the first pillar and put it inside the structure"""
	struct = CUBOID([px,py,beamsDist[-1]])
	for i in range(len(pillarsDist)):
		beam = CUBOID([pillarsDist[i],by,bz])
		for j in range(len(beamsDist)):
			"""create the last beam with the proper high"""
			if j == len(beamsDist)-1:
				beam = CUBOID([pillarsDist[i]+px,by,bz])
			struct = STRUCT([struct,T(3)(beamsDist[j]),beam])
		"""last pillar"""
		pillar =  CUBOID([px,py,beamsDist[-1]])
		struct = STRUCT([struct,T(1)(pillarsDist[i]),pillar])
	return struct
   
def main():
	"""Create two different type of structures from different sets of values"""
	struct1 = buildStruct(1,1,[10,20,40],1,1,[2,4,6])
	VIEW(struct1)
	struct2 = buildStruct(1,1,[10,20,40,60],1,1,[2,4,6,9])
	VIEW(struct2)

if __name__ == '__main__':
	main()