# This is based on Bentley's Programming Pearls chapter 8.
# My (Hai Vu's) modification: if the array is all negatives
# then max is the largest element
def largest(array):
    """
    >>> largest([0,1,2,3])
    6
    >>> largest( [-1, 2, 3, -4, 5, 1] )
    6
    """
    maxSoFar = maxUpToHere = 0
    largestElement = array[0]
    allNegatives = True

    for element in array:
        maxUpToHere = max(maxUpToHere + element, 0)
        maxSoFar = max(maxSoFar, maxUpToHere)
        largestElement = max(largestElement, element)
        if element >= 0:
            allNegatives = False

    if allNegatives:
        return largestElement
    return maxSoFar


if __name__ == "__main__":
    import doctest

    doctest.testmod()
