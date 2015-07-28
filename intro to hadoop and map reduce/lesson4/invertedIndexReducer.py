#!/usr/bin/python

import sys



def reducer():
	count = 0
	oldKey = None

	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) != 2:
			continue

		thisKey, thisValue = data
		if thisKey == "fantastically":
			print thisKey, "\t", thisValue

		if oldKey and oldKey != thisKey:
			if oldKey == "fantastic":
				print oldKey,"\t",count
			oldKey = thisKey
			count = 0

		oldKey = thisKey
		count += 1

	if oldKey != None:
		print oldKey,"\t",count

def main():
    mapper()
    sys.stdin = sys.__stdin__

main()