#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data
#"id"  "title"  "tagnames"  "author_id"  "node_type"  "parent_id"  "abs_parent_id"  "added_at" 
#"score"  "reputation"  "gold"  "silver"  "bronze"

import sys

def reducer():
	id = ""
	title = ""
	tagnames = ""
	author_id = ""
	node_type = ""
	parent_id = ""
	abs_parent_id = ""
	added_at = ""
	score = ""
	reputation = ""
	gold = ""
	silver = ""
	bronze = ""	
	
	oldUserId = None
    	for line in sys.stdin:
		# YOUR CODE HERE\
        	data = line.strip().split("\t")
        	curUserId = data[0]
        	if oldUserId and oldUserId != curUserId:
        		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(id,title,tagnames,author_id,node_type,parent_id,abs_parent_id, added_at, score,reputation, gold, silver ,bronze)
        		oldUserId = curUserId

        	if data[1] == 'A':
			author_id, clasfy, reputation, gold, silver, bronze = data
        	elif data[1] == 'B':
			author_id, clasfy, id, title, tagnames, node_type, parenet_id, abs_parent_id, added_at, score = data
        	oldUserId = curUserId 

    	if oldUserId != None:
		print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(id,title,tagnames,author_id,node_type,parent_id,abs_parent_id, added_at, score,reputation, gold, silver ,bronze)

        

reducer()
