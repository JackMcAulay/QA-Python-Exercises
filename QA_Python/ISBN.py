def isbn(n):
    return n.replace('?', str(10 - ((int(n[0]) + (3 * int(n[1])) + int(n[2]) + (3 * int(n[4])) + 4 + (3 * int(n[6]))
                                     + int(n[8]) + (3 * int(n[10])) + int(n[11]) + (3 * int(n[12])) + int(n[13])
                                     + (3 * int(n[14]))) % 10)))


print(isbn('978-0-306-40615-?'))
