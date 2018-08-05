with open('hash1.txt') as f:
    with open('extractedhash1.txt', 'a') as g:
        for line in f:
            l = line.rstrip('\n').split(':')
            g.write(l[1] + '\n')
