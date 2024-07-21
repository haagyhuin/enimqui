def linear_search_signal(signal, target):
    """
    Searches for a target value in a signal using the linear search algorithm.

    Parameters:
    signal (list): The signal to be searched.
    target (int): The target value to search for.

    Returns:
    int: The index of the target value in the signal, or -1 if not found.
    """
    for i in range(len(signal)):
        if signal[i] == target:
            return i
    return -1

# Example usage
signal = [64, 34, 25, 12, 22, 11, 90]
index = linear_search_signal(signal, 25)
print("Index of 25 in signal using Linear Search:", index)
