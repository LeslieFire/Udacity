#!/usr/bin/python

import sys

count = 0
oldKey = None
totalSales = 0

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	thisKey, thisValue = data_mapped

	if oldKey and oldKey != thisKey:
		print oldKey, "\t", totalSales / count
		oldKey = thisKey
		count = 0
		totalSales = 0

	oldKey = thisKey
	count += 1
	totalSales += float(thisValue)

if oldKey != None:
	print oldKey, "\t", totalSales / count