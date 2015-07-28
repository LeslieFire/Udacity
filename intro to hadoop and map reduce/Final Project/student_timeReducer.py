#!/usr/bin/python

import sys



oldId = None

hours = {}

for i in range(24):
	hours[i] = 0

for line in sys.stdin:

	data = line.strip().split("\t")
	if len(data) == 2:
		thisAuthorId, hour = data

		if oldId and oldId != thisAuthorId:
			print "{0}\t{1}".format(oldId, max(hours, key=hours.get))
			oldId = thisAuthorId
			for i in range(24):
				hours[i] = 0

		oldId = thisAuthorId
		hours[int(hour)] += 1

if oldId != None:
	print "{0}\t{1}".format(oldId, max(hours, key=hours.get))



