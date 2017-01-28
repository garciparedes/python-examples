"""
Author: Sergio Garcia Prado
        www.garciparedes.me

Fibonacci example implemented recursive and Iterative mind.
""""


import time

"""                            Funtions                            """


"""
Recursive Version
"""
def recursiveFib(n):
    if (n<2):
        return n
    else:
        return (recursiveFib(n-1) + recursiveFib(n-2))



"""
Iterative Version
"""
def iterativeFib(n):
    i = 1
    j = 0
    for k in range(n):
        j = i + j
        i = j - i
    return j



"""                            MAIN                            """

print """Fibonacci Example"""


number = int(raw_input("Insert Integer Number: "))
print ''
print """Iterative Version"""
start = time.time()
print iterativeFib(number)
print "it took", time.time() - start, "seconds."

print ''

print """Recursive Version"""
start = time.time()
print recursiveFib(number)
print "it took", time.time() - start, "seconds."
