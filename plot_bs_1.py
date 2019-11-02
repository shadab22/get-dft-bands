#fetches band structure data from case.spaghetti_ene based on the index of the bands provided. 
#Gives E vs k as per the Brillouin zone.

import math as m
import sys


filename = sys.argv[1] #case.spaghetti_ene file

rfile = open(filename, 'r')
wfile = open("bands_spaghetti.txt", 'w')

bands_to_plot = []

for i in range(481,505):
	bands_to_plot.append(i)

no_of_k_points = 101

lines_of_file = rfile.readlines()


for line_no in range(0, len(lines_of_file)):
	if lines_of_file[line_no][0:12] == "  bandindex:":
		if int(lines_of_file[line_no][13:len(lines_of_file[line_no])]) in bands_to_plot:
			i = line_no
			for line_no in range(i+1, i+no_of_k_points+1):
				wfile.write(lines_of_file[line_no])
			wfile.write("\n")