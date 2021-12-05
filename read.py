data = []
count = 0

with open('reviews.txt' , 'r') as file_one:
	for line in file_one:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data)/10000,'%')


print(len(data))
