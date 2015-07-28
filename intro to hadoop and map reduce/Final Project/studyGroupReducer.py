#!/usr/bin/python

import sys
import csv

oldKey = None
authorList = []

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 2:
		continue

	thisKey, author_id = data
	if oldKey and thisKey != oldKey:
		print oldKey, "\t", authorList
		del authorList[:]
		oldKey = thisKey

	oldKey = thisKey
	authorList.append(author_id)

if oldKey != None:
	print oldKey, "\t", authorList