def minMoves(h, w, h1, w1):
    # Write your code here
    s = 0
    while h != h1:
        if h1 >= h/2:
            h = h1
            s+=1
        else:
            h = h/2
            s+=1

    while w != w1:
        if w1 >= w/2:
            w = w1
            s+=1
        else:
            w = w/2
            s+=1
    return s

print(minMoves(5,4,3,1))