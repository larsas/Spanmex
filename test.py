#!/usr/bin/env python3

import csv
import pandas as pd
import chardet


path = '/home/larsas/Desktop/Project_Spanmex/Listado_Completo_69-B.csv'
append_write='r'

with open(path, 'rb') as f:
    result = chardet.detect(f.read())  # or readline if the file is large

textfile= pd.read_csv(path, encoding=result['encoding'], delimiter=',')
print(type(textfile))
test=textfile.split('\t')

#with open(path, append_write) as file:
	#reader = read_csv(file, encoding = 'utf-8')
	#for row in reader:
		#print(row)
