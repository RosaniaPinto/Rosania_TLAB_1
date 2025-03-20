def filter_nondigits(data: list) -> list:
    new_list = []
    """
    INSERT DOCSTRING HERE
    """
    for line in data:
        line = line.strip()
        #print (line)
        if line.isdigit():
            #print(line)
            new_list.append(int(line))
    #x = filter_nondigits("data/phase3.txt.")
    #print(x)
    #print(round(sum(x)/len(x)))
    return new_list
