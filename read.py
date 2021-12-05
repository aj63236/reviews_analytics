data = []
count = 0

with open('reviews.txt' , 'r') as file_one:
	for line in file_one:
		data.append(line)
		count += 1
		if count % 10000 == 0:
			print(len(data)/10000,'%')


print("檔案讀取完成,總共有",len(data),"筆資料")

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print("全部留言的平均長度是", sum_len/len(data))

#[len(data[1]),.....,len(data[1000000])]
#for num in data:
	#data_two.append(len(num))
	#print(data_two[0])

