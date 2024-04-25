def add_set(A,B):
    result = set()

    for i in A:
        result.add(i)
    
    for i in B:
        if i not in result:
            result.add(i)

    print( result)

A={19,34,56,7} 
B={1,2,5,19,34,7}

add_set(A,B)
