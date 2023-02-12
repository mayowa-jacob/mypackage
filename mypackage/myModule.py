def top_n(items, n):
    """
    Return the top n items in an array, in a desc order

    Args:
        items (Array): Lists or array like objects.

        n (int): The number of items to return.

    Return:
        array: top n items, in desc order.

    Egs:
        >>> top_n([8, 3, 2, 7, 4], n)
        [8, 7, 4]

    """

    for i in range(n):
        for j in range(len(items)-1-i):
            if items[j] > items[j + 1]:  # if this item is bigger than the next item
                items[j], items[j+1] = items[j+1], items[j]  # swap the two

    # get last two items:
    top_n = items[-n:]

    # return in desc order
    return top_n[::-1]
