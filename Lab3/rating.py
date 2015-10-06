################################
### Creates Database
### Updates Database with Data
################################

import sqlite3 as lite
import sys
import os 
import csv
import urllib
import re

ratingsList = "http://boxnumbertwo.com/MovieData/ratings.list"
response = urllib.urlopen(ratingsList)

count = 0

## Set directory to computer
directoryForDB = "D:/Workshop/homework/Data Analytics/Lab3/"
if not os.path.exists(directoryForDB):
	os.makedirs(directoryForDB)

directoryForDB = directoryForDB + "movies.db"
## If database does not exist, creates items
## If database does exist, opens it
con = lite.connect(directoryForDB)
with con:
	ratingdb = con.cursor()
	ratingdb.execute("DROP TABLE IF EXISTS MoviesInfo") 
	ratingdb.execute("CREATE TABLE MoviesInfo(name TEXT, rate REAL, vote INT, year TEXT, PB INT, DG INT, WG INT)")
	count = 0
	for line in response: #  Get vote, rate, name and year of movies
	   words = re.sub(' +',' ',line.strip()) #  This is a string!
	   save = words.split(" ",3) #  Split vote, rate, name and year
	   vote = int(save[1].replace("'", "")) #  Get votes
	   rate = float(save[2].replace("'", "")) #  Get rates
	   nameANDdate = save[3].split(" (",1) #  Only part of  names have quotation, so we can not split name with quotation
	   name = nameANDdate[0].replace('"', '') #  Get names
	   print name
	   year = nameANDdate[1].replace("?","0") #  Get years
	   year = int(re.sub("\D","",year) )
	   print year
	   count = count +1
	   print count
	   #if count>100: #  Limit numbers to store
	     #  break
	   insertStatement = 'INSERT INTO MoviesInfo(name, rate, vote, year) VALUES("%s",%f,%d,%d)' % (name,rate,vote,year) #  Add movies' names and ratings into database
	   ratingdb.execute(insertStatement)
		
	## NEEDED, if not, database does not update
	con.commit()