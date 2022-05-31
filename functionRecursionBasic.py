# Python also accepts function recursion, which means a defined function can call itself.
# remember recursion must have an end point

def recursiveFunction(numUpto, i):
    # i = 0
    if i == numUpto:
        return
    else:
        print(numUpto)
        numUpto = numUpto-1
        recursiveFunction(numUpto, i)


recursiveFunction(10, 0)
