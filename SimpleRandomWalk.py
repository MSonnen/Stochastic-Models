import random

def simulate(p, i, n):
    k=1
    position = i
    samplePath = [i]
    while k < n:
        if random.random()<p:
            position+=1
        else:
            position-=1
        samplePath.append(position)
        k+=1
    return samplePath

print(simulate(0.5,0,10))
simulate(0.3,6,10)
