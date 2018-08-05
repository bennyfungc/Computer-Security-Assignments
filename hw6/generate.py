from hashlib import md5

part = [1, 0, 0, 0, 0]
symbols = { 'a':'@' , 'c':'(' , 'g':'9' , 'o':'0' , 'b':'8' , 'f':'#' , 'i':'1' , 'l':'1' , 's':'$' }
PID = "A12158802"

#importing unsalted hash values
hash1 = {}
with open('hash1.txt') as f:
    for line in f:
        l = line.rstrip('\n').split(':')
        hash1[l[1]] = l[0]

#
recovered = {}
with open('hash1.txt') as f:
    for line in f:
        l = line.rstrip('\n').split(':')
        recovered[l[0]] = None

#checking if hashed guess matches a value
def verify(guess):
    hashValue = md5((PID+guess).encode('utf-8')).hexdigest()
    if hashValue in hash1:
        recovered[hash1[hashValue]] = guess

#cracking part 1
if part[0]:
    with open('words.txt') as f:
        for line in f:
            verify(line.rstrip('\n'))

    print ("Number of passwords recovered from [1]: " + str(len(recovered)))

#cracking part 2
if part[1]:
    for i in range(100000000):
        verify(str(i))
        j = str(i)
        while len(j) < 8:
            j = "0" + j
            verify(j)

    print ("Number of passwords recovered from [2]: " + str(len(recovered)))

#cracking part 3
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

    print ("Number of passwords recovered from [3]: " + str(len(recovered)))

#cracking part 4
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

    print ("Number of passwords recovered from [4]: " + str(len(recovered)))

#cracking part 5
if part[4]:
    with open('words.txt') as f:
        for line1 in f:
            word1 = line1.rstrip('\n')
            with open('words.txt') as g:
                for line2 in g:
                    word2 = line2.rstrip('\n')
                    verify(word1 + word2)

with open('cracked.txt', 'a') as f:
    with open('hash1.txt') as g:
        for line in g:
            l = line.rstrip('\n').split(':')
            if recovered[l[0]] != None:
                if l[0] in recovered:
                    f.write(l[0] + ":" + recovered[l[0]] + "\n")
#for key in recovered:
    #print recovered[key] + ": " + key
