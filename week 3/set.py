def intersection(A,B):
    intersect = set()
    for i in A:
        if i not in B:
            intersect.add(i)
    for i in B:
        if i not in A:
            intersect.add(i)
    print(intersect)

def compliment(A,B):
    comp = set()
    for i in B:
        if i not in A:
            comp.add(i)
    print(comp)


A={19,34,56,7} 
B={1,2,5,19,34,7}
intersection(A,B)
compliment(A,B)