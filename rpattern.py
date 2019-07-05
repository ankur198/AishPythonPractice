def printR(n):
    n = n//2
    result = []
    result.append('* '*n)
    for i in range(n-1):
        result.append('*'+' '*(2*(n-1))+'*')
    result.append('* '*n)
    os = (2*(n-1)-1)
    for i in range(n):
        result.append('*'+' '*(i+1)+'*' + '-'*os)
        os -= 1
    return result


def printW(n):

    result = []
    outers = 0
    inners = 2 + 4*((n-3)//2) + n

    for i in range(((n+1)//2)-1):
        result.append(' '*outers + '*'+' '*inners+"*" + '-'*outers)
        outers += 1
        inners -= 2

    inner1 = n-2
    result.append(' '*outers+'*'+' '*inner1+'*'+' '*inner1+'*' + '-'*outers)

    outers += 1
    inner1 -= 2
    inner2 = 1
    for i in range((n+1)//2 - 2):
        result.append(' '*outers+'*'+' '*inner1+'*' + ' ' * inner2 + '*' + ' '*inner1+'*' + '-'*outers)
        outers += 1
        inner1 -= 2
        inner2 += 2
    result.append(' '*outers+'*'+' '*inner2+'*' + '-'*outers)
    return result


n = 7
R = printR(n)
W = printW(n)
for i in range(n):
    print(R[i], R[i], W[i])

# n = 5
# for i in range(n):
#     num = ord('a')
#     for j in range(i+1):
#         print(chr(num),end='')
#         num+=1
#     print()
