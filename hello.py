x = int(input("enter size of sequence:"))
lastSec = 0
last = 1
print(lastSec)
print(last)
for i in range(x-2):
    new = lastSec + last
    print(new)
    lastSec = last
    last = new
