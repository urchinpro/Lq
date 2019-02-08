f = open(r'c:/tmp/iq200-pyth/iq200/result4600000000112.txt')
s3=''
for line in f:
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
    i = 0
    while i < len(line):
        x=''
        s1=''
        s2=''
        s=line[i:i+4]
        s1=s[0:2]
        s2=s[2:]
        x=chr(int(s2+s1, 16)) #перевод из hex в decimal. Предыдущие две итерации для замены байтов местами
        s3=s3+x #постоянное приращение
        i=i+4 #так как utf-16-le 2 байта (обратный порядок в байтах)
print(s3)
print('Работает!! \u2713')



