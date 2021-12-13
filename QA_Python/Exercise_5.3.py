def all_even(a, b):
    nums = []
    for i in range(a, b):
        x = [int(d) for d in str(i)]
        for j in x:
            if j % 2 != 0:
                break
        else:
            nums.append(int(i))
    return nums


print(all_even(10, 30))
