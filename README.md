# Get bands from a band structure plot from a WIEN2k run within the range of specified band-index

plot_bs_1.py fetches bands from case.spaghetti_ene from a WIEN2k run.
Input in the bandindex range in an array.
Output is a 5-column file with the columns beign:  kx 	\t 	 ky	 \t  kz \t 	band_struct_plot x-axis [0:1]	 \t 	 Energy.
Different bands are separated by a linebreak. 
Degenerate bands are considered distinctly in case.spaghetti_ene file, that is, there could me more than one bandindex which give rise to exact same/overlapping bands.


plot_bs.py fetches bands from case.band.agr from WIEN2k run. This one will not be used much as the information obtained from this python code is already present in the column 4 and 5 of the output of plot_bs_1.py.
Input is the bandindex range in an array.
Output is a 2-column file with the columns being:    band_struct_plot x-axis [0:1]	 \t 	 Energy.
