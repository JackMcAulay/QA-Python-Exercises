def near(a, b):
    for i in a:
        if b == a.replace(i, ''):
            return True
    return False


print(near('soup', "oup"))

