import pymysql
import xlrd
import json
import re
con = pymysql.connect('localhost', 'worker', 'lightpass', 'russpass');
xl='./data.xlsx'
sub='Аквапарк'
titleCol=1
addCol=6
geoCol=33
conCol=[7,8,9]
descCol=2
with con:
	cur = con.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS `poi` (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,`type` TEXT NOT NULL,`name` TEXT NOT NULL,`description` TEXT NOT NULL, `address` TEXT NOT NULL,`contacts` TEXT NOT NULL,`latitude` FLOAT NULL,`longitude` FLOAT NULL);")
	wb = xlrd.open_workbook(filename=xl,encoding_override='UTF-8')
	sheet = wb.sheet_by_index(0)
	for i in range(sheet.nrows-1):
		row=sheet.row_values(i+1)
		contacts=""
		coords=re.findall(r'(\d*\.\d*)',row[geoCol])
		print(coords)
		for k in conCol:
			contacts+=row[k]+" "
		sqStr="INSERT INTO `poi` (`id`,`type`,`name`,`address`,`latitude`,`longitude`,`description`,`contacts`) VALUES(NULL,'"+sub+"','"+row[titleCol]+"','"+row[addCol]+"',"+str(float(coords[0]))+","+str(float(coords[1]))+",'"+row[descCol]+"','"+contacts+"');"
		cur.execute(sqStr)