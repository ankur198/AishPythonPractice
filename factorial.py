# n = int(input('Enter no.:'))
# if n % 2 == 0:
#     if n == 2 and n == 5:
#         print('not Weird')
#     elif n == 6 and n == 20:
#         print('weird')
#     else:
#         print('not weird')
# else:
#     print('weird')

# n = [5,6,6,2,3]

# for i in range(len(n)):
#     n[i] = n[i]**2
# print(n)

# def sq(element):
#     return element**2

# print(list(map(lambda element:element**2,range(1,int(input("enter range"))+1))))

x = 1
y = 1
z = 1
n = 2

# y = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n]

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                print([i,j,k]) 
# print(y)
