

def top_n(ls, n):
    """"
    Return top nth item ordered
    arg:
       ls (list data type)
       n type int: number of item to return
    """
    for i in range(n):
        for j in range(len(ls)-1-i):
            if ls[j]> ls[j+1]:
                  ls[j], ls[j+1] = ls[j+1], ls[j] 
    return ls[-n:][::-1]