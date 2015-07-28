#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter = "\t")
next(reader, None)

for line in reader:
	if len(line) == 19:
		node_type = line[5]
		body = line[4]
		node_id = line[0]
		parent_id = line[6]
		if node_type == "question":
			print "{0}\t{1}\t{2}".format(node_id, node_type, len(body))
		elif node_type == "answer":
			print "{0}\t{1}\t{2}".format(parent_id, node_type, len(body))

