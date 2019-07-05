a = [1, 4, 6, 32, 1, 5, 7, 46, 85, 6, 24, 3]

for Pass in range(len(a)-1):
    for j in range(len(a)-Pass-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
    print('Pass',Pass,':',a)


