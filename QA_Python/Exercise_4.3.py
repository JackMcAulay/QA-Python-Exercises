n = int(input("Please enter Grid Size :")) + 1

for i in range(1, n):
    line = ''
    for j in range(1, n):
        line += f"{i*j}\t"
    print(line)

print('\n')

for i in range(1, n):
    for j in range(1, n):
        print(i*j, end='\t')
    print('')

