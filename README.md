# Top N Items in a List

A simple Python function to return the top N items from a list, ordered in ascending order.

## Function:

```python
def top_n(ls, n):
    """
    Return top nth item ordered

    Args:
       ls (list): List containing data
       n (int): Number of items to return

    Returns:
       list: Top N items in ascending order
    """
    for i in range(n):
        for j in range(len(ls)-1-i):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j] 
    return ls[-n:][::-1]
