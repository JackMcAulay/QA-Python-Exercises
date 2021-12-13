names = []
count = 1
while count < 6:
    names.append(input(f"Enter name {count} :"))
    count += 1
for name in names:
    print(f"{name} is awesome!")
