data = []
hund = []
good = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		if len(data) % 1000 == 0:
			print(len(data))
print('檔案讀取完畢，共', len(data), '筆資料')
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	if len(d) < 100:
		hund.append(d)
print('平均留言長度為: ', sum_len / len(data))

print('一共有', len(hund), '留言字數<100')
print(hund[0])
print('--------------')
print(hund[1])

for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '留言提到good')
print(good[0])
print(good[1])

	