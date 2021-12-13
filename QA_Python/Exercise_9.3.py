file = open('teams', 'w')
teams_list = ['City FC', 'Town FC', 'Other City FC', 'Town Wednesday FC', 'Other Town FC']

for i in teams_list:
    file.write(f"{i}\n")

file = open('teams', 'r')
teams = file.readlines()
print(f"Team 1 - {teams[0]}Team 2 - {teams[3]}")

file.close()
