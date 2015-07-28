#!/usr/bin/python

import sys

questionLen = 0
answerLen = 0
answerCount = 0
oldKey = None

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) != 3:
		continue

	thisKey, node_type, length = data
	if oldKey and oldKey != thisKey:
		if answerCount == 0:
			print "{0}\t{1}\t{2}".format(oldKey, questionLen, 0)
		else :
			print "{0}\t{1}\t{2}".format(oldKey, questionLen, answerLen/answerCount)

		oldKey = thisKey
		questionLen = 0
		answerLen = 0
		answerCount = 0

	oldKey = thisKey
	if node_type == "question":
		questionLen = int(length)
	elif node_type == "answer":
		answerCount += 1
		answerLen += float(length)

if oldKey != None:
	if answerCount == 0:
		print "{0}\t{1}\t{2}".format(oldKey, questionLen, 0)
	else:
		print "{0}\t{1}\t{2}".format(oldKey, questionLen, answerLen/answerCount)