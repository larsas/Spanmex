#!/usr/bin/env python3

import csv
import pandas as pd
import chardet
import numpy as np
import sys
import re

#Your company list: 
	
#List of paths: 
#path = ['/home/larsas/Desktop/Project_Spanmex/Listado_Completo_69-B.csv','/home/larsas/Desktop/Project_Spanmex/my_list.csv']
path=['/home/larsas/Desktop/Project_Spanmex/my_list.csv']

for j in range(0,len(path)):

	append_write='rb' #read-only binary format.

	with open(path[j], append_write) as f:
	#Use chardet to be able to read .csv file above, encoding is strange, chardet fixes it. 
		result = chardet.detect(f.read())  

	textfile= pd.read_csv(path[j], encoding=result['encoding'], delimiter=',')
	array = textfile.to_numpy() #Convert dataframe panda to numpy array

	companyid = []
	companyname = []

	for i in range(0,len(array)):
		if str(array[i,1])=='nan' and str(array[i,2])=='nan':
			pass
		else:
			companyid.append(array[i,1])
			companyname.append(array[i,2])


#Government list: 

pathgov=['/home/larsas/Desktop/Project_Spanmex/Listado_Completo_69-B.csv']

for j in range(0,len(pathgov)):

	append_writegov='rb' #read-only binary format.

	with open(pathgov[j], append_writegov) as fgov:
	#Use chardet to be able to read .csv file above, encoding is strange, chardet fixes it. 
		resultgov = chardet.detect(fgov.read())  

	textfilegov = pd.read_csv(pathgov[j], encoding=resultgov['encoding'], delimiter=',')
	arraygov = textfilegov.to_numpy() #Convert dataframe panda to numpy array

	companyidgov = []
	companynamegov = []

	for i in range(0,len(arraygov)):
		if str(arraygov[i,1])=='nan' and str(arraygov[i,2])=='nan':
			pass
		else:
			companyidgov.append(arraygov[i,1])
			companynamegov.append(arraygov[i,2])

companyidgov.remove('RFC')
companyid.remove('RFC')

for i in range(0,len(companyid)):
	if companyid[i] in companyidgov:
		print(companyid[i])
		#print(companyidgov.index(companyid[i]))
		print(companyidgov[companyidgov.index(companyid[i])])
		
	else:
		print('no')
		#print(companyidgov.index(companyid[i]))
		print('RFC is not in list:', companyid[i])
		#print(companyidgov[companyidgov.index(companyid[i])])


#print(companyidgov)
#print(companyid)
#Check if company from government is in your company list:

#for t in range(0,len(companyid)):
#	if str(companyid[i])==str(companyidgov[i]):
#		print('yes')
#	else:
#		print('no')		
		
#Print full array
#np.set_printoptions(threshold=sys.maxsize)
#print(array)





