#fetches band structure data from case.band.agr based on the index of the bands provided
#Gives E vs k with k values scaled from 0-1.

import math as m
import sys


filename = sys.argv[1] #case.band.agr file

rfile = open(filename, 'r')
wfile = open("bands_agr.txt", 'w')

bands_to_plot = []

for i in range(483,502):
	bands_to_plot.append(i)

no_of_k_points = 101

lines_of_file = rfile.readlines()


for line_no in range(0, len(lines_of_file)):
	if lines_of_file[line_no][0:13] == " # bandindex:":
		if int(lines_of_file[line_no][13:len(lines_of_file[line_no])]) in bands_to_plot:
			i = line_no
			for line_no in range(i+1, i+no_of_k_points+1):
				wfile.write(lines_of_file[line_no])
			wfile.write("\n")



