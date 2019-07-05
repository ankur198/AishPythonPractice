n = 5
space = 0
allResult = []
for i in range(n):
    num = ord('a')
    result = '-'*space
    alpha = ''
    for j in range(n-i-1):
        alpha += chr((num+(n-j-1))) +'-'
    
    result += alpha
    result += chr(num + i)
    result += alpha[::-1]
    result += '-'*space
    space += 2
    allResult.append(result)

allResult.reverse()
for i in allResult:
    print(i)
allResult.pop()

allResult.reverse()
for i in allResult:
    print(i)
