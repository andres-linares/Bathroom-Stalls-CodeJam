# -*- coding: utf-8 -*-

from time import time

def main():
	file = open("C-small-practice-1.in", "r")
	outputFile = open("output1.txt", "w")
	testCases = int(file.readline())
	t1 = time()

	n = []
	k = []

	for x in range(98, testCases):
		line = file.readline().split()
		n.append(int(line[0]))
		k.append(int(line[1]))

	analyze(n, k, 1, 0)
	
	t2 = time()
	print("Time = " + str(t2 - t1) + " s.")
	outputFile.close()

def solve(n, k):
	stalls = []
	assignValues(stalls, n)
	for x in range(0, k):
		print(str(x) + " de " + str(k) + ". Total orinales = " + str(n))
		index = searchBetterStall(stalls)
		print("orinal escogido = " + str(index + 1))
		if x != k -1:
			stalls[index][2] = True
		else:
			return (max(stalls[index][0], stalls[index][1]),
				min(stalls[index][0], stalls[index][1]))
		updateValues(stalls)

def analyze(n, k, parts, part):
	outputFile = open("output1.txt", "w")
	starting = part * 2 / parts
	finalize = (part + 1) * 2 / parts 
	for x in range(starting, finalize):
		solutionA, solutionB = solve(n[x], k[x])
		output = "Case #{0}: {1} {2}\n".format(x+1, solutionA, solutionB)
		outputFile.write(output)
		print output
	outputFile.close()


def updateLeftValues(stalls):
	leftValue = 0
	for x in stalls:
		if x[2] == True:
			leftValue = 0
		else:
			x[0] = leftValue
			leftValue += 1

def updateRightValues(stalls):
	rightValue = 0
	for x in range(0, len(stalls)):
		if stalls[len(stalls) - 1 - x][2] == True:
			rightValue = 0
		else:
			stalls[len(stalls) - 1 - x][1] = rightValue
			rightValue += 1 

def updateValues(stalls):
	updateLeftValues(stalls)
	updateRightValues(stalls)



def searchBetterStall(stalls):
	minIndexs = betterMinValues(stalls)
	maxFromIndexs = betterMaxValues(stalls, minIndexs)
	leftmostIndex = maxFromIndexs[0]
	return leftmostIndex

def betterMaxValues(stalls, minIndexs):
	indexs = []
	maxMaximum = 0
	for x in minIndexs:
		stall = stalls[x]
		maximum = max(stall[0], stall[1])
		if maximum > maxMaximum:
			indexs = []
			maxMaximum = maximum
		if maximum == maxMaximum:
			indexs.append(x)
	return indexs


def betterMinValues(stalls):
	"""
	O(n) = n
	Called for every new person K.
	"""
	index = 0
	indexs = []
	maxMinimum = 0
	for x in stalls:
		if x[2] == False:
			minimun = min(x[0], x[1])
			if minimun > maxMinimum:
				indexs = []
				maxMinimum = minimun
			if minimun == maxMinimum:
				indexs.append(index)
		index += 1
	return indexs


def assignValues(stalls, n):
	"""
	O(n) = n
	Called just once.
	"""
	for x in range(0, n):
		values = [x, n - x - 1, False]
		stalls.append(values)

if __name__ == "__main__":
	main()