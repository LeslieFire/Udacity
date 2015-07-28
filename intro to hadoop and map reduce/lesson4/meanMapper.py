#!/usr/bin/python
import sys
from datetime import datetime

for line in sys.stdin:
	data = line.strip().split("\t")
	if len(data) == 6:
		weekday = datetime.strptime(data[0], "%Y-%m-%d").weekday()
		sale = data[4]
		print "{0}\t{1}".format(weekday, sale)