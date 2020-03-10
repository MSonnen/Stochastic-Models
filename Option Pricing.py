import random
def simulateAsianCall(T, K, n, p, u, d, r, S0):
    i=0
    total = 0
    pStar = (1+r-d)/(u-d)
    while i < n:
        S=[S0]
        j = 0
        while j < T:
            U = random.random()
            if U < pStar:
                S.append(S[-1]*u)
            else:
                S.append(S[-1]*d)
            j+=1
    total += max(0, (1/T)*(sum(S[1:]))-K)
    i+=1
    return total/(n * (1+r)**T)
print(simulateAsianCall(2,45, 1000, 0.6,1.2,1.02,0.06, 40))
simulateAsianCall(2,45, 10000, 0.6,1.2,1.02,0.06, 40)

