#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter = "\t")
next(reader, None)

for line in reader:
	if len(line) != 19:
		continue

	node_type = line[5].strip()
	if node_type == "question":
		tags = line[2].strip().split()
		for tag in tags:
			print tag
