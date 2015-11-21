#!/usr/bin/python

import sys



def reducer():
	count = 0
	oldKey = None
	col = []

	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) != 2:
			continue

		thisKey, thisValue = data
		if thisKey == "fantastically":
			print thisKey, "\t", thisValue

		if oldKey and oldKey != thisKey:
			#if oldKey == "fantastic":
			#	print oldKey,"\t",count
			col.sort(key = lambda x: long(x), reverse = True)
			for i in range(len(col)):
				print oldKey, "\t", col[i]
			
			oldKey = thisKey
			count = 0
			del col[:]

		oldKey = thisKey
		count += 1
		col.append(thisValue)

	if oldKey != None:
		print oldKey,"\t",count

def main():
    mapper()
    sys.stdin = sys.__stdin__

main()