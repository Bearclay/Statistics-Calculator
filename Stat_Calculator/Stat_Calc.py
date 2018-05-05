"""
Created on Mon Mar  5 21:16:04 2018

@author: Robert Barclay
"""
#from collections import Counter
# A simple function that sums the values in the list. I added this instead of
# the 'sum' function to practice coding.
def sum_my_lst(a_lst):
    a_sum = 0.0
    for item in a_lst:
        a_sum = a_sum + float(item)
    return a_sum

# Another function that will calculate the mean for values in a list
def calc_mean(a_lst):
    div = sum_my_lst(a_lst)
    mean = float(div) / (len(a_lst))
    return mean

def calc_mode(a_lst):
    # Creates new list to store values if there is more than one of them in the data
    poss_mode = []
    # Sorts given list
    a_lst.sort()
    # For loop that compares the first item in the list to every item throughout
    for fnum, snum in zip(a_lst, a_lst[1:]):
        # If the item is equal to another in the list, it's stored in poss_mode
        if fnum == snum:
            poss_mode.append(fnum)
    # Check if one or more iteration of a number in the list. If so, returns first value
    if len(poss_mode) >= 1:
        return poss_mode[0]
        

# An empty list where it adds the user input
lst_of_num = []     

print("I am data machine, give me your data I will calculate mean, median, mode, range and standard deviation. ")

# The original string is empty, causing the prompt to loop until
# the user enters 'done'. Stores the input as floats.
prompt = ""
while prompt != "done":
    prompt = input("Give me your data: ")
    if prompt == "done" : break
    lst_of_num.append(float(prompt))

# Takes in user input, makes it all lower case to handle different input
# regardless of case. 
option = input("Would you like me to calculate Mean, Median, Range, Mode, or Standard Deviation? \n")
option_lower = option.lower()

# Calculates mean if user selects mean
if option_lower == "mean":
    a_mean = calc_mean(lst_of_num)
    print("The mean is: " + str(a_mean))
 
# Calculates median if user selects median
elif option_lower == "median":
    # sorts user input from highest to lowest using ".sort()" function
    lst_of_num.sort()          
    
    # Calculates median if list is even length
    if len(lst_of_num) % 2 == 0:
        first_mid = len(lst_of_num) / 2
        sec_mid = lst_of_num[int(first_mid)]
        numerator = float(first_mid) + float(sec_mid)
        median = numerator / len(lst_of_num)
        print("The median is: " + str(median))
        
    # Calculates median if list is odd length
    else:
        even_var = (len(lst_of_num) - 1) / 2
        median = lst_of_num[int(even_var)]
        print("The median is: " + str(median))

# Calculates range if user requests range        
elif option_lower == "range":
    # sorted_lst_range = lst_of_num.sort() 
    lst_of_num.sort() 
    print(lst_of_num)        
    max_var = lst_of_num[-1]
    min_var = lst_of_num[0]
    data_range = float(max_var) - float(min_var)
    print("The range is: " + str(data_range))

# Calculates standard deviation
elif option_lower == "standard deviation":
    # Empty list for difference values
    diff_lst = []
    # Calculate mean of list
    sd_mean = calc_mean(lst_of_num)
    
    # This goes through user inputed values and subtracts the the mean from
    # each value and then squares it. 
    for num in lst_of_num:
        result = (float(num) - sd_mean) ** 2.0
        # Then rounds the result to two digits
        rounded_result = round(result, 2)
        # Add these values to our difference values list
        diff_lst.append(rounded_result)
    # Here we take the mean of the differences
    new_sum = calc_mean(diff_lst)
    # Take the square root of that mean and we have our standard deviation
    standard_deviation = (new_sum) ** (1/2.0)
    print("The standard deviation is: " + str(standard_deviation))

# Calculates Mode for Data
elif option_lower == "mode":
    # Calls calc_mode function
    mode = calc_mode(lst_of_num)
    print("The mode is: " + str(mode))