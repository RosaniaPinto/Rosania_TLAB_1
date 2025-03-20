"""
The main Python mpdule that combines cleaner and metrics functions in order to
perform comprehensive analysis
"""

def plot_adjusted_data(data: list, cleaned_data: list, filename: str) -> None:
    """
    Uses cleaned data and original source data to accurately map each sample to every associated 5 minute sampling interval.
    Creates data for missing and "NO DATA" samples by taking the average of the previous sample and proceeding sample, inserting the newly-made data in between.
    Args:
        data (list[str]): list of strings representing heart rate samples
        cleaned_data (list[int]): list of cleaned and type-casted data, derived from data
        filename (str): name used to create savefile, which stores into images/ folder
    Returns:
        None
    """

    x_vars = []
    y_vars = []

    

    for i in range(0, len(data)):                  #creating x variables for plotting, incremented by 5
        x_vars.append(i*5)

                                                    #going back to unclean data... (I wanted to fill in each missing data point with a calculated value, this is the extra part lol)


# you could honestly leave out this part and skip to the actual plotting vvv

    adjuster = 0
    for i in range(0, len(cleaned_data)):             #creating y variables, with adjustments for missing data (an avg between the previous data point and the next data point)
        
        if str(cleaned_data[i]) == data[i + adjuster].strip("\n"):
            y_vars.append(cleaned_data[i])
        elif (i + 1) < len(cleaned_data):
            psud_var = 0
            psud_var += cleaned_data[i-1]
            psud_var += cleaned_data[i]
            y_vars.append(psud_var / 2)
            y_vars.append(cleaned_data[i])
            adjuster += 1
        else:
            y_vars.append(cleaned_data[i])
            y_vars.append(cleaned_data[i+1])
            break

#set your y_vars to your cleaned data instead [somewhere here]


    plt.figure(figsize=(16,6))
    plt.xlim(0, 450)
    plt.ylim(0, 120)
    plt.plot(x_vars, y_vars)

    plt.title('HEART RATE DATA')
    plt.xlabel('Time (minutes)')
    plt.ylabel('BPM')

    plt.savefig('images/' + filename + '.png')