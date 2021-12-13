file = open('textfile', 'r')

outfile = ''

for line in range(1, 6):
    if line % 2 == 0:
        outfile += file.readline()
    else:
        file.readline()

file = open('textfile2', 'w')
file.write(outfile)
file.close()
