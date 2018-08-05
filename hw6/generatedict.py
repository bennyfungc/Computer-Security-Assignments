from hashlib import md5

part = [0, 0, 0, 0, 1, 0]
symbols = { 'a':'@' , 'c':'(' , 'g':'9' , 'o':'0' , 'b':'8' , 'f':'#' , 'i':'1' , 'l':'1' , 's':'$' }
PID = "A11922669"

#importing unsalted hash values
#hash1 = {}
#with open('hash1.txt') as f:
    #for line in f:
        #l = line.rstrip('\n').split(':')
        #hash1[l[1]] = l[0]
#
##initializing dictionary for cracked passwords
#recovered = {}
#with open ('hash1.txt') as f:
    #for line in f:
        #l = line.rstrip('\n').split(':')
        #recovered[l[0]] = None

#checking if hashed guess matches a value
def verify(guess):
    hashValue = md5(PID+guess).hexdigest()
    if hashValue in hash1:
        recovered[hash1[hashValue]] = guess

#cracking part 1 (current count: 67)
if part[0]:
    with open('words.txt') as f:
        with open('word1.txt', 'a') as g:
            for line in f:
                #verify(line.rstrip('\n'))
                g.write(PID + line)

#cracking part 2 (current count: 250)
if part[1]:
    with open('word2.txt', 'a') as f:
        for i in range(100000000):
            # verify(str(i))
            j = str(i)
            f.write(PID + j + '\n')
            while len(j) < 8:
                j = "0" + j
                f.write(PID + j + '\n')
            #verify(j)

#cracking part 3 (current count: )
if part[2]:
    wlength = 5
    with open('possible5w.txt', 'a') as g:
        with open('words.txt') as f:
            for line in f:
                word = line.rstrip('\n')
                if len(word) == wlength:
                    available = 10 - len(word)
                    if available > 0:
                        for i in range(10 ** available):
                            g.write(PID + word + str(i) + '\n')
                            j = str(i)
                            while len(word + j) < 10:
                                j = "0" + j
                                g.write(PID + word + j + '\n')

#cracking part 4 (current count: 147)
def permute(word, index, f):
    if index < len(word):
        #recurse to pass unmodified down the calls
        permute(word, index + 1, f)
        #check upper case, then recurse
        upperCase = word
        upperCase = "".join(c.upper() if i == index else c for i, c in enumerate(upperCase))
        #verify(upperCase)
        f.write(PID + upperCase + '\n')
        permute(upperCase, index + 1, f)
        #if index can be symbol, check symbol, then recurse
        if(word[index] in symbols):
            symbol = word
            symbol = "".join(symbols[c] if i == index else c for i, c in enumerate(symbol))
            # verify(symbol)
            f.write(PID + upperCase + '\n')
            permute(symbol, index + 1, f)

if part[3]:
    with open('words.txt') as f:
        for line in f:
            with open('word4.txt', 'a') as f:
                permute(line.rstrip('\n'), 0, f)

#cracking part 5 (current count: 233)
if part[4]:
    with open('word5.txt', 'a') as h:
        with open('words.txt') as f:
            for line1 in f:
                word1 = line1.rstrip('\n')
                with open('words.txt') as g:
                    for line2 in g:
                        word2 = line2.rstrip('\n')
                        #verify(word1 + word2)
                        h.write(PID + word1 + word2 + '\n')

#write out all cracked passwords into file in order (current master count: 697)
if part[5]:
    count = 0
    with open('cracked.txt', 'a') as f:
        with open('hash1.txt') as g:
            for line in g:
                l = line.rstrip('\n').split(':')
                if recovered[l[0]] != None:
                    if l[0] in recovered:
                        f.write(l[0] + ":" + recovered[l[0]] + '\n')
                        count = count + 1

    print ("Number of passwords recovered: " + str(count))
