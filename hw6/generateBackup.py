from hashlib import md5

part = [0, 0, 0, 0, 1, 0]
symbols = { 'a':'@' , 'c':'(' , 'g':'9' , 'o':'0' , 'b':'8' , 'f':'#' , 'i':'1' , 'l':'1' , 's':'$' }
PID = "A12158802"

#importing unsalted hash values
hash1 = {}
with open('hash1.txt') as f:
    for line in f:
        l = line.rstrip('\n').split(':')
        hash1[l[1]] = l[0]

dupes = {}
with open ('hash1.txt') as f:
    for line in f:
        l = line.rstrip('\n').split(':')
        dupes[l[0]] = None

#initializing dictionary for cracked passwords
recovered = {}
with open ('hash1.txt') as f:
    for line in f:
        l = line.rstrip('\n').split(':')
        recovered[l[0]] = None

#checking if hashed guess matches a value
def verify(guess):
    hashValue = md5((PID + guess).encode('utf-8')).hexdigest()
    if hashValue in hash1:
        if recovered[hash1[hashValue]] == None:
            recovered[hash1[hashValue]] = guess
        else:
            print(hash1[hashValue])
            dupes[hash1[hashValue]] = guess

#cracking part 1 (current count: 67)
if part[0]:
    with open('words.txt') as f:
        for line in f:
            verify(line.rstrip('\n'))

#cracking part 2 (current count: 250)
if part[1]:
    for i in range(100000000):
        verify(str(i))
        j = str(i)
        while len(j) < 8:
            j = "0" + j
            verify(j)

#cracking part 3 (current count: )
if part[2]:
    with open('words.txt') as f:
        for line in f:
            word = line.rstrip('\n')
            available = 10 - len(word)
            if available > 0:
                for i in range(10 ** available):
                    verify(word + str(i))
                    j = str(i)
                    while len(word + j) < 10:
                        j = "0" + j
                        verify(word + j)

if part[5]:
    with open('possible5w.txt') as f:
        for line in f:
            word = line.rstrip('\n')
            verify(word)

#cracking part 4 (current count: 147)
def permute(word, index):
    if index < len(word):
        #recurse to pass unmodified down the calls
        permute(word, index + 1)
        #check upper case, then recurse
        upperCase = word
        upperCase = "".join(c.upper() if i == index else c for i, c in enumerate(upperCase))
        verify(upperCase)
        permute(upperCase, index + 1)
        #if index can be symbol, check symbol, then recurse
        if(word[index] in symbols):
            symbol = word
            symbol = "".join(symbols[c] if i == index else c for i, c in enumerate(symbol))
            verify(symbol)
            permute(symbol, index + 1)

if part[3]:
    with open('words.txt') as f:
        for line in f:
            permute(line.rstrip('\n'), 0)

#cracking part 5 (current count: 233)
if part[4]:
    with open('words.txt') as f:
        for line1 in f:
            word1 = line1.rstrip('\n')
            with open('words.txt') as g:
                for line2 in g:
                    word2 = line2.rstrip('\n')
                    verify(word1 + word2)

#write out all cracked passwords into file in order (current master count: 697)
count = 0
with open('pw4.txt', 'a') as f:
    with open('hash1.txt') as g:
        for line in g:
            l = line.rstrip('\n').split(':')
            if recovered[l[0]] != None:
                if l[0] in recovered:
                    f.write(l[0] + ":" + recovered[l[0]] + '\n')
                    count = count + 1
            if dupes[l[0]] != None:
                if l[0] in dupes:
                    f.write(l[0] + ":" + dupes[l[0]] + '\n')
                    count = count + 1

print ("Number of passwords recovered: " + str(count))
