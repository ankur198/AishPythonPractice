rule = {
    'a': ['e'],
    'e': ['a', 'i'],
    'i': ['a', 'e', 'o', 'u'],
    'o': ['i', 'u'],
    'u': ['a']
}


class string:
    def __init__(self, s=''):
        self.string = s

    def canAdd(self, vowel):
        if self.string == '':
            return True
        return vowel in rule[self.string[-1]]


size = 4
allVowel = ['a', 'e', 'i', 'o', 'u']
count = 0


def traverse(parent):
    global count
    if len(parent.string) == size:
        count += 1
        # print(parent.string)
    if len(parent.string) < size:
        for i in allVowel:
            if parent.canAdd(i):
                child = string(parent.string)
                child.string += i
                traverse(child)


curr = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
oldCurr = dict(curr)
length = 1

def traverseNew():
    global count,length
    while size>length:
        oldCurr = dict(curr)
        for j in oldCurr:
            times = oldCurr[j]
            new = rule[j]
            for i in new:
                curr[i]+=times
            curr[j]-=times
        length+=1
    count = sum(curr.values())

# traverse(string())
traverseNew()
print(count % (10**9+7))


# def getLongestPeriod(h, l):
#     longest = 0
#     for i in range(len(h)):
#         current = []
#         well = 0
#         notWell = 0
#         for j in range(i, len(h)):
#             current.append(h[j])
#             if h[j] > l:
#                 well += 1
#             else:
#                 notWell += 1
#             if well > notWell:
#                 longest = max(longest, well+notWell)
#     return longest


# print(getLongestPeriod([13, 9, 1, 3, 2, 10], 7))
# print(getLongestPeriod([4,7,5,8,3], 5))
