import math
import time

while True:
    n = int(input("What will n be in the equation 1/x + 1/y = 1/n :"))
    x = n + 1
    count = 0
    A = []
    trials = 0

    while True:
        #print("((1/", n, " - 1/", x, ")**-1) = " , round(((1/n - 1/x)**-1), 5))
        if round(((1/n - 1/x)**-1), 10).is_integer():
            count += 1
            y = int(round((1/n - 1/x)**-1, 5))
            A += [(x, y)]
            if x == y:
                break
            x += 1
        else:
            x +=1
        
    print("Number of Pairs: ", count)
    print("Pairs: ", A)
    print()


