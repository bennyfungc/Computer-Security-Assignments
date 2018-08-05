from hashlib import md5

PID = "A12158802"
hash1 = []
with open ('hash1.txt') as f:
	for line in f:
		l = line.rstrip('\n').split(':')
		hash1.append((l[0], l[1]))

count = 0
with open ('cracked1245.txt') as f:
	for line in f:
		l = line.rstrip('\n').split(':')
		for i in range(len(hash1)):
			if l[0] == hash1[i][0] and md5((PID + l[1]).encode('utf-8')).hexdigest() == hash1[i][1]:
				hash1[i] = (l[0], l[1])
				count = count + 1

with open ('cracked3_5.txt') as f:
	for line in f:
		l = line.rstrip('\n').split(':')
		for i in range(len(hash1)):
			if l[0] == hash1[i][0] and md5((PID + l[1]).encode('utf-8')).hexdigest() == hash1[i][1]:
				hash1[i] = (l[0], l[1])
				count = count + 1

with open ('cracked3_6.txt') as f:
	for line in f:
		l = line.rstrip('\n').split(':')
		for i in range(len(hash1)):
			if l[0] == hash1[i][0] and md5((PID + l[1]).encode('utf-8')).hexdigest() == hash1[i][1]:
				hash1[i] = (l[0], l[1])
				count = count + 1

with open ('cracked3_7.txt') as f:
	for line in f:
		l = line.rstrip('\n').split(':')
		for i in range(len(hash1)):
			if l[0] == hash1[i][0] and md5((PID + l[1]).encode('utf-8')).hexdigest() == hash1[i][1]:
				hash1[i] = (l[0], l[1])
				count = count + 1

with open ('cracked3_8.txt') as f:
	for line in f:
		l = line.rstrip('\n').split(':')
		for i in range(len(hash1)):
			if l[0] == hash1[i][0] and md5((PID + l[1]).encode('utf-8')).hexdigest() == hash1[i][1]:
				hash1[i] = (l[0], l[1])
				count = count + 1

with open ('cracked3_9.txt') as f:
	for line in f:
		l = line.rstrip('\n').split(':')
		for i in range(len(hash1)):
			if l[0] == hash1[i][0] and md5((PID + l[1]).encode('utf-8')).hexdigest() == hash1[i][1]:
				hash1[i] = (l[0], l[1])
				count = count + 1

with open('finalhash1.txt', 'a') as f:
	for i in range(len(hash1)):
			f.write(hash1[i][0] + ":" + hash1[i][1] + '\n')

	print(count)
