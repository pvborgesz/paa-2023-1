s = [1,2,3,4,5,6,7,8,23,2314,42]

def searchRootValuesInArray(n,s): # n log n
    count = 0 # 1  
    s.sort() # n log n
    target = n ** (1/2) # 10
    foundValues = [] # 1
    while count < target: # max cost is target times * 2
        foundValues.append(s[count])
        count += 1

def searchRootValuesInHeap(n, h):
    count = 0 # 1  
    target = n ** (1/2) # 10
    foundValues = [] # 1
    while count < target: # max cost is target times * 2
        foundValues.append(h.pop()) # log n
        count += 1

# Remove the biggest is log n, so the cost is log n multiplied by the size of target, that is the squared root of n
# so, the complexity is O(root(n) * log(n)) 