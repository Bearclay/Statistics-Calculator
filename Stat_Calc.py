"""
Created on Mon Mar  5 21:16:04 2018

@author: Robert
"""

# A simple function that sums the values in the list. I added this instead of
# the 'sum' function to practice my code.
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
    # sorts user input from highest to lowest using "sorted()" function
    sorted_lst = sorted(lst_of_num)         
    
    # Calculates median if list is even length
    if len(sorted_lst) % 2 == 0:
        first_mid = len(sorted_lst) / 2
        sec_mid = sorted_lst[int(first_mid)]
        numerator = float(first_mid) + float(sec_mid)
        median = numerator / len(sorted_lst)
        print("The median is: " + str(median))
        
    # Calculates median if list is odd length
    else:
        even_var = (len(sorted_lst) - 1) / 2
        median = sorted_lst[int(even_var)]
        print("The median is: " + str(median))

# Calculates range if user requests range        
elif option_lower == "range":
    # sorted_lst_range = lst_of_num.sort() 
    lst_of_num.sort()      
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
        
    
