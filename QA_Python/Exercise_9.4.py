file = open('teams', 'r')
teams = file.readlines()
outfile = "This is a new line\n"

for i in range(1, len(teams)):
    outfile += teams[i]

file = open('teams', 'w')
file.write(outfile)
file.close()
