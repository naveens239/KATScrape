import urllib, urllib2
from bs4 import BeautifulSoup
import string




print "\nWelcome to KATscrape - The KAT Cause List Generator"
print "\nEnter the date for which you want the cause list to be generated:\n"




#Date for which the cause list is to be generated.
d = int (raw_input("Day (dd): "))
m = int (raw_input("Month (mm): "))
y = int (raw_input("Year (yyyy): "))
print "------------------------------\n"




#Pages that are to be parsed.
wiki1 = "http://keralaadministrativetribunal.gov.in/ciskat/pages/cause_list_home.php?type=search&dte=%d/%d/%d&court=1" % (d, m, y)
wiki2 = "http://keralaadministrativetribunal.gov.in/ciskat/pages/cause_list_home.php?type=search&dte=%d/%d/%d&court=7" % (d, m, y)
wiki3 = "http://keralaadministrativetribunal.gov.in/ciskat/pages/cause_list_home.php?type=search&dte=%d/%d/%d&court=8" % (d, m, y)
wiki4 = "http://keralaadministrativetribunal.gov.in/ciskat/pages/cause_list_home.php?type=search&dte=%d/%d/%d&court=4" % (d, m, y)

adv = ["BASIL AJITH", "BRIJESH MOHAN", "HARIKRISHNAN S", "JAJU BABU K", "JAYAKRISHNAN D", "LIZZIE ALBERT", 
		"MAHESH DEV M S", "NIDHI BALACHANDRAN", "PRAKASH G S", "SHEEJA M S", "SUBAIR KUNJU P", "RAJAPRATHAP S J", "RENOJ S", 
		"RESMI G NAIR", "UNNIKRISHNAN C", "VENUGOPALAN NAIR V"]


print "Matters before the Kerala Administrative Tribunal on %d/%d/%d:" % (d, m, y)

#Court 1 Reader
page1 = urllib2.urlopen(wiki1)
soup1 = BeautifulSoup(page1, "lxml")
text1 = soup1.prettify()
np0 = text1.count(adv[0])
np1 = text1.count(adv[1])
np2 = text1.count(adv[2])
np3 = text1.count(adv[3])
np4 = text1.count(adv[4])
np5 = text1.count(adv[5])
np6 = text1.count(adv[6])
np7 = text1.count(adv[7])
np8 = text1.count(adv[8])
np9 = text1.count(adv[9])
np10 = text1.count(adv[10])
np11 = text1.count(adv[11])
np12 = text1.count(adv[12])
np13 = text1.count(adv[13])
np14 = text1.count(adv[14])
np15 = text1.count(adv[15])

print "\nCOURT 1 (Principal Bench)"
print "------------------------------\n"
#Adv. Jaju Babu & Team
if adv[3] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[3], np3)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[3]

if adv[1] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[1], np1)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[1]

if adv[13] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!\n" % (adv[13], np13)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench).\n" % adv[13]

#Adv. Jayakrishnan D & Team # 4 14 7 2 15 12 6 9 11 10 5 8 0
if adv[4] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[4], np4)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[4]

if adv[14] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[14], np14)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[14]

if adv[7] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[7], np7)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[7]

if adv[2] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[2], np2)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[2]

if adv[15] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[15], np15)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[15]

if adv[12] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[12], np12)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[12]

if adv[6] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[6], np6)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[6]

if adv[9] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[9], np9)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[9]

if adv[11] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[11], np11)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[11]

if adv[10] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[10], np10)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[10]

if adv[5] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[5], np5)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[5]

if adv[8] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!" % (adv[8], np8)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench)." % adv[8]

if adv[0] in text1:
  print "Adv. %s has %d case(s) in Court 1 (Principal Bench)!\n" % (adv[0], np0)
else:
  print "There's no case for Adv. %s in Court 1 (Principal Bench).\n" % adv[0]




#Court 2 Reader
page2 = urllib2.urlopen(wiki2)
soup2 = BeautifulSoup(page2, "lxml") #Parsing can also be done without specifying the parser 
text2 = soup2.prettify()             #(lxml is the parser for linux I guess)
n2c0 = text2.count(adv[0])
n2c1 = text2.count(adv[1])
n2c2 = text2.count(adv[2])
n2c3 = text2.count(adv[3])
n2c4 = text2.count(adv[4])
n2c5 = text2.count(adv[5])
n2c6 = text2.count(adv[6])
n2c7 = text2.count(adv[7])
n2c8 = text2.count(adv[8])
n2c9 = text2.count(adv[9])
n2c10 = text2.count(adv[10])
n2c11 = text2.count(adv[11])
n2c12 = text2.count(adv[12])
n2c13 = text2.count(adv[13])
n2c14 = text2.count(adv[14])
n2c15 = text2.count(adv[15])

print "\nCOURT 2 (Additional Bench 1)"
print "------------------------------\n"
#Adv. Jaju Babu & Team
if adv[3] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[3], n2c3)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[3]

if adv[1] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[1], n2c1)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[1]

if adv[13] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!\n" % (adv[13], n2c13)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1).\n" % adv[13]

#Adv. Jayakrishnan D & Team # 4 14 7 2 15 12 6 9 11 10 5 8 0
if adv[4] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[4], n2c4)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[4]

if adv[14] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[14], n2c14)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[14]

if adv[7] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[7], n2c7)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[7]

if adv[2] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[2], n2c2)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[2]

if adv[15] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[15], n2c15)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[15]

if adv[12] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[12], n2c12)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[12]

if adv[6] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[6], n2c6)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[6]

if adv[9] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[9], n2c9)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[9]

if adv[11] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[11], n2c11)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[11]

if adv[10] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[10], n2c10)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[10]

if adv[5] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[5], n2c5)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[5]

if adv[8] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!" % (adv[8], n2c8)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1)." % adv[8]

if adv[0] in text2:
  print "Adv. %s has %d case(s) in Court 2 (Additional Bench 1)!\n" % (adv[0], n2c0)
else:
  print "There's no case for Adv. %s in Court 2 (Additional Bench 1).\n" % adv[0]

#Court 3 Reader
page3 = urllib2.urlopen(wiki3)
soup3 = BeautifulSoup(page3, "lxml")
text3 = soup3.prettify() #This displays the html source of a page orderly
n3c0 = text3.count(adv[0])
n3c1 = text3.count(adv[1])
n3c2 = text3.count(adv[2])
n3c3 = text3.count(adv[3])
n3c4 = text3.count(adv[4])
n3c5 = text3.count(adv[5])
n3c6 = text3.count(adv[6])
n3c7 = text3.count(adv[7])
n3c8 = text3.count(adv[8])
n3c9 = text3.count(adv[9])
n3c10 = text3.count(adv[10])
n3c11 = text3.count(adv[11])
n3c12 = text3.count(adv[12])
n3c13 = text3.count(adv[13])
n3c14 = text3.count(adv[14])
n3c15 = text3.count(adv[15])

print "\nCOURT 3 (Additional Bench 2)"
print "------------------------------\n"
#Adv. Jaju Babu & Team
if adv[3] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[3], n3c3)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[3]

if adv[1] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[1], n3c1)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[1]

if adv[13] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!\n" % (adv[13], n3c13)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2).\n" % adv[13]

#Adv. Jayakrishnan D & Team # 4 14 7 2 15 12 6 9 11 10 5 8 0
if adv[4] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[4], n3c4)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[4]

if adv[14] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[14], n3c14)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[14]

if adv[7] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[7], n3c7)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[7]

if adv[2] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[2], n3c2)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[2]

if adv[15] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[15], n3c15)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[15]

if adv[12] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[12], n3c12)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[12]

if adv[6] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[6], n3c6)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[6]

if adv[9] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[9], n3c9)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[9]

if adv[11] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[11], n3c11)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[11]

if adv[10] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[10], n3c10)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[10]

if adv[5] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[5], n3c5)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[5]

if adv[8] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!" % (adv[8], n3c8)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2)." % adv[8]

if adv[0] in text3:
  print "Adv. %s has %d case(s) in Court 3 (Additional Bench 2)!\n" % (adv[0], n3c0)
else:
  print "There's no case for Adv. %s in Court 3 (Additional Bench 2).\n" % adv[0]




#Ernakulam Bench Reader
page4 = urllib2.urlopen(wiki4)
soup4 = BeautifulSoup(page4, "lxml")
text4 = soup4.prettify() #This displays the html source of a page orderly
n4c0 = text4.count(adv[0])
n4c1 = text4.count(adv[1])
n4c2 = text4.count(adv[2])
n4c3 = text4.count(adv[3])
n4c4 = text4.count(adv[4])
n4c5 = text4.count(adv[5])
n4c6 = text4.count(adv[6])
n4c7 = text4.count(adv[7])
n4c8 = text4.count(adv[8])
n4c9 = text4.count(adv[9])
n4c10 = text4.count(adv[10])
n4c11 = text4.count(adv[11])
n4c12 = text4.count(adv[12])
n4c13 = text4.count(adv[13])
n4c14 = text4.count(adv[14])
n4c15 = text4.count(adv[15])

print "\nCOURT 1 (Ernakulam Camp Sitting)"
print "------------------------------\n"
#Adv. Jaju Babu & Team
if adv[3] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[3], n4c3)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[3]

if adv[1] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[1], n4c1)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[1]

if adv[13] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!\n" % (adv[13], n4c13)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench.\n" % adv[13]

#Adv. Jayakrishnan D & Team # 4 14 7 2 15 12 6 9 11 10 5 8 0
if adv[4] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[4], n4c4)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[4]

if adv[14] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[14], n4c14)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[14]

if adv[7] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[7], n4c7)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[7]

if adv[2] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[2], n4c2)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[2]

if adv[15] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[15], n4c15)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[15]

if adv[12] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[12], n4c12)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[12]

if adv[6] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[6], n4c6)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[6]

if adv[9] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[9], n4c9)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[9]

if adv[11] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[11], n4c11)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[11]

if adv[10] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[10], n4c10)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[10]

if adv[5] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[5], n4c5)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[5]

if adv[8] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!" % (adv[8], n4c8)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench." % adv[8]

if adv[0] in text4:
  print "Adv. %s has %d case(s) before the Ernakulam Bench!\n" % (adv[0], n4c0)
else:
  print "There's no case for Adv. %s before the Ernakulam Bench.\n" % adv[0]


#To search for single advocate
#print "Enter the relevant code for the counsel concerned:"
#print 
	#BASIL AJITH:    0     MAHESH DEV M S:     6    RENOJ S:            12
	#BRIJESH MOHAN:  1     NIDHI BALACHANDRAN: 7    RESMI G NAIR:       13
	#HARIKRISHNAN S: 2     PRAKASH G S:        8    UNNIKRISHNAN C:     14 
	#JAJU BABU K:    3     SHEEJA M S:         9    VENUGOPALAN NAIR V: 15
	#JAYAKRISHNAN D: 4     SUBAIR KUNJU P:     10   
	#LIZZIE ALBERT:  5     RAJAPRATHAP S J:    11
	
#x = int (raw_input("Code: "))

# 4 14 7 2 15 12 6 9 11 10 5 8 0