def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    average = 0
    total = 0
    count = 0
    for a_data in data:
        total += a_data
        count += 1
    if count == 0:
        return []
    
    average = total / count
    return average


def maximum(data: list) -> float:
    """
    INSERT DOCSTRING HERE
    """
    maximum = 0
    for item in data:
        if item > maximum:
            maximum = item
    if maximum == 0:
        return []
    return maximum

        
def variance(data: list) -> float:

    """
    Calculates the population variance of a list of integers.
    Variance measures the average squared deviation from the mean.
    """
    if not data or len(data) < 2:
        return 0
    avg = average(data)
    var = sum((x - avg) ** 2 for x in data) / len(data)
    return round(var, 2)

def standard_deviation(data: list) -> float:

    """
    Calculate the standard deviation of a list of integers.
    
    Args:
        data (list of int): A list of integers.
    
    Returns:
        float: The standard deviation, rounded to 2 decimal places.
    """
    if data != []:
        return round(variance(data) ** 0.5, 2)
    return []
