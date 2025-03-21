## Question 1

Take a look at the file labeled `data/phase0.txt`. Why might we have missing values or values that state "NO DATA" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

The data missing could be because of some of the data not being tracked. The risk if ignoring the NO DATA is that you're not getting the complete story of the data.

## Question 2

During sleep, we expect maximum heart rate of a phase to be **lower** than the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase does sleep occur? Mention numerical details that back your findings.

Phase 0 in which sleep occur. The reason why phase 0 has the lowest maximum heart rate out of the phases at 93.

# return all 3 values
phase 0
return avg_hr, max_hr, std_dev_hr
(64.59, 93, 8.53)

phase 1
 return avg_hr, max_hr, std_dev_hr
(87.3, 110, 9.9)

phase 2
 return avg_hr, max_hr, std_dev_hr
(85.18, 117, 13.38)

phase 3
 return avg_hr, max_hr, std_dev_hr
(60.65, 99, 11.0)

## Question 3

During exercise, we expect the maximum heart rate of a phase to be **higher** the maximum heart rate of all other phases. Observe the visualizations and descriptive statistics that you've calculated. Using these findings, in which phase(s) does exercise occur? Mention numerical details that back your findings. 

Phase 2 in which excerise occurs . The reason why phase 2 has the highest maximum heart rate out of the phases at 117.

phase 0
return avg_hr, max_hr, std_dev_hr
(64.59, 93, 8.53)

phase 1
 return avg_hr, max_hr, std_dev_hr
(87.3, 110, 9.9)

phase 2
 return avg_hr, max_hr, std_dev_hr
(85.18, 117, 13.38)

phase 3
 return avg_hr, max_hr, std_dev_hr
(60.65, 99, 11.0)


## Question 4

During regular periods of awake activity, we expect the average heart rate of a phase to be relatively **lower** than the average heart rate of other phases, but we also expect standard deviation to be **higher**. In which phase do we notice this trend?

Phase 3 is when we have period of awake activity. This is because the average heart rate of phase 3 is relatively lower than other phases, while the standard deviation is higher than the other 2 phases.

phase 0
return avg_hr, max_hr, std_dev_hr
(64.59, 93, 8.53)

phase 1
 return avg_hr, max_hr, std_dev_hr
(87.3, 110, 9.9)

phase 2
 return avg_hr, max_hr, std_dev_hr
(85.18, 117, 13.38)

phase 3
 return avg_hr, max_hr, std_dev_hr
(60.65, 99, 11.0)

