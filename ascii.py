f = open(r'c:/tmp/iq200-pyth/iq200/result4600000000112.txt')
s1=''
s2=''
x=''
for line in f:
    s1=line
    endt = 0
    startt = 0
    startt = line.find(chr(2))
    if chr(23) in line:
        endt = line.find(chr(23))
    elif chr(3) in line:
        endt = line.find(chr(3))
    elif chr(4) in line:
        continue
    line = line[startt+2:endt]
    print(line)
    i = 0
    while i < len(line):
        x=''
        s=line[i:i+4]
        if s != '00':
            x=chr(int(s, 16))
        s2=s2+x
        i=i+4
print(s2)


