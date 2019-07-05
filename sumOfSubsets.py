import copy


class node:

    origSet = [1, 2, 3,4,5,6,7,8]
    toSum = 13

    def __init__(self):
        self.reqSum = node.toSum
        self.currentList = []
        self.index = 0

    def add(self, value=None):
        if value != None:
            self.currentList.append(value)
            self.reqSum = node.toSum - sum(self.currentList)
        self.index += 1

    def isFeasible(self):
        if self.index >= len(node.origSet) or self.reqSum < 0:
            return False
        return True

    def isFinished(self):
        return self.reqSum == 0

    @staticmethod
    def copyNode(oldNode):
        newNode = node()
        newNode.reqSum = oldNode.reqSum
        newNode.currentList = copy.deepcopy(oldNode.currentList)
        newNode.index = oldNode.index
        return newNode


subset = []


def traverse(parentNode):
    if parentNode.isFinished():
        subset.append(parentNode)

    if parentNode.isFeasible():
        value = node.origSet[parentNode.index]
        child1 = node.copyNode(parentNode)
        child2 = node.copyNode(parentNode)

        child1.add(value)
        child2.add()

        traverse(child1)
        traverse(child2)



traverse(node())

finalList = [str(i.currentList) for i in subset]
uniqueList = set(finalList)

print(uniqueList)
