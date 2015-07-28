#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter = "\t")
next(reader, None)

for line in reader:
	if len(line) == 19:
		author_id = line[3]
		hour = line[8][11:13]

		print "{0}\t{1}".format(author_id, hour)

