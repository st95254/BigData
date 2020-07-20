import pandas as pd # 載入pandas套件並命名為pd
csvdata = pd.read_csv('0714train.csv') # 以read_csv函式讀取csv
# csv = csvdata.dropna()

# 分類Input_C之資料
for x in range(1, 138):
	data = csvdata['Input_C_%03d' %x]
	dtype = data.dtype
	if dtype == object:
		print('Input_C_%03d' %x)
		i = 0
		while i < len(csvdata): # 簡單化
			dataStr = str(data[i])
			temp = dataStr.split(';')
			move1 = temp[0]
			move2 = temp[2]
			if move1 == 'N':
				move1 = '0'
			elif move1 == 'U':
				move1 = '+'
			elif move1 == 'D':
				move1 = '-'
			if move2 == 'N':
				move2 = '0'
			elif move2 == 'R':
				move2 = '+'
			elif move2 == 'L':
				move2 = '-'
			print(move1 + temp[1] + move2 + temp[3])
			i += 1
	else:
		pass