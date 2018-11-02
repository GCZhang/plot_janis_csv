#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import matplotlib as mpl
mpl.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np

#--------------------------------------------------------------------------------------------------
def plot_from_csv(csv_file_name):
    # converter function that decodes a string as unicode
    conv = {0:(lambda s: s.decode('unicode-escape'))}

    col_names = np.genfromtxt(csv_file_name, dtype='unicode', delimiter=';', max_rows=1, converters=conv)

    col_names = [csv_file_name.replace('.csv',' ') + s for s in col_names]

    data_set_num = len(col_names) - 1

    csv_data = np.genfromtxt(csv_file_name, delimiter=';', skip_header=3)

    x_data = csv_data[:,0]
    for data_set in range(1,data_set_num+1):
        y_data = csv_data[:,data_set]
        plt.loglog(x_data, y_data, linewidth=0.8,label=col_names[data_set])
#--------------------------------------------------------------------------------------------------

csv_file_list = sys.argv[1:]

for csv_file in csv_file_list:
	plot_from_csv(csv_file)

plt.xlabel('Energy (eV)')
plt.ylabel('Cross section (barn)')
plt.grid(b=True, linestyle='--')
plt.legend()
plt.show()
