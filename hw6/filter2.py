from hashlib import md5

PID = "A12158802"
hash2 = []
result = []
with open ('hash2.txt') as f:
	for line in f:
		l = line.rstrip('\n').split(':')
		hash2.append((l[0], l[1], l[2]))
		result.append((l[0], l[1], l[2]))

count = 0
for i in range(len(hash2)):
	with open ('saltcracked.txt') as f:
		for line in f:
			l = line.rstrip('\n')
			if md5((PID + l + hash2[i][2]).encode('utf-8')).hexdigest() == hash2[i][1]:
				result[i] = (hash2[i][0], l)
				count = count + 1
'''
with open ('saltycracker.txt') as f:
	for line in f:
		l = line.rstrip('\n')
		for i in range(len(hash2)):
			if md5(PID + l + hash2[i][2]).hexdigest() == hash2[i][1]:
				results.append((hash2[i][0], l))
'''
with open('finalhash2.txt', 'a') as f:
	for i in range(len(result)):
			f.write(result[i][0] + ":" + result[i][1] + '\n')

	print(count)
