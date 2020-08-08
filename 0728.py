import numpy as np
import pandas as pd
import csv
csvdata = pd.read_csv("0728test.csv")

with open('new.csv','w') as csvfile:
	writer_t = csv.writer(csvfile)
	#writer_d = csv.writer(csvfile,lineterminator='\n')
	list_title = []
	list_d = []
	for x in range(1, 138):
		if x == 13 or x == 46 or x == 49 or x == 50 or x == 57 or x == 58 or x == 96:
			pass
		else:
			before = csvdata['Input_C_%03d' %x].isnull().value_counts()
			print(before)	
			data = csvdata['Input_C_%03d' %x]
			dtype = data.dtype
			dataStr = str(data)
			if dtype == object:
				print('Input_C_%03d' %x)
				i = 0
				while i < len(csvdata): # 簡單化，直接跳過空值
					dataStr = str(data[i])
					if dataStr != 'nan':
						temp = dataStr.split(';')
						move1 = temp[0]
						move2 = temp[2]
						if move1 == 'N':
							move1 = '+'
						elif move1 == 'U':
							move1 = '+'
						elif move1 == 'D':
							move1 = '-'
						if move2 == 'N':
							move2 = '+'
						elif move2 == 'R':
							move2 = '+'
						elif move2 == 'L':
							move2 = '-'
						ud = float(move1 + temp[1])
						lr = float(move2 + temp[3])
					i += 1

			else:
				print('Input_C_%03d' %x)
				# with open('new.csv','w') as csvfile:
				# writer = csv.writer(csvfile)
				list_title.append('Input_C_%03d' %x)
				i = 0
				list_d = []
				while i < len(csvdata):
					dataStr = str(data[i])
					if dataStr != 'nan':
						data[i] = dataStr
						print(data[i])
						list_d.append(data[i])
					else:
						#data[i] = csvdata['Input_C_%03d' %x].median()
						print(data[i])
						#list_d.append(data[i])

					print(list_d)
					i += 1
			writer_d = csv.writer(csvfile,lineterminator='\n')
			writer_d.writerow(map(lambda x:x,list_d))
		writer_t.writerow(map(lambda j:j,list_title))
		#writer_d.writerows(map(lambda x:[x],list_d))
		