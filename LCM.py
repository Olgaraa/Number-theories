def lcm(x,y):
    lcm=1
    for i in reversed(range(x, 1000000, x*1)):   
        for k in reversed(range(y, 1000000, y*1)):
            if k==i:
                lcm=k
                break
    return lcm
