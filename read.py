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

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print("一共有%s筆留言長度小於100" %len(new))

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print("一共有%s筆留言稱讚產品好" %len(good))

bad = [d for d in data if "bad" in d]
print("一共有%s筆留言稱讚產品不好" %len(bad))