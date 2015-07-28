#!/usr/bin/python

import sys
import csv

tags = {}
oldKey = None
count = 0

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 1:
		continue

	thisKey = data[0]

	if oldKey and thisKey != oldKey:
		tags[oldKey] = count
		count = 0
		oldKey = thisKey

	oldKey = thisKey
	count += 1

if oldKey != None:
	tags[oldKey] = count
	
top10 = sorted(tags, key=tags.get, reverse=True)[:10]
for tag in top10:
	print "{0}\t{1}".format(tag, tags[tag])