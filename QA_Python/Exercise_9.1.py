file = open('anotherTestfile', 'w')

for i in range(11):
    new_line = f'This is line {i}.\n'
    file.write(new_line)

file.close()
