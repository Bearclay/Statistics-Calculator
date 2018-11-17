# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 20:44:48 2018

@author: Robert
"""

"""
Created on Mon Mar  5 21:16:04 2018

@author: Robert Barclay
"""
"""
    This a simple calculator designed to calculate the mean, median, range, mode, or standard deviation. 
    It prompts the user to enter in data one by one, then it asks for what the user wants to calculate. 
    The program then calculate the method specified by the user. 
    
    Attributes:
        Calculator class: This class has a method that sums the list passed in which is used by the other 
        4 methods calc_mean, calc_median, standard_deviation, calc_range and calc_mode. These methods calculate 
        the mean, the median, the standard deviation, the range and the mode base on the numbers provided by the 
        user.
        
"""
class Calculator:
    def __init__(self, a_lst):
        self.a_lst = a_lst
    
    #A simple function that sums the values in the list. I added this instead of
    #the 'sum' function to practice coding.
    def sum_my_lst(self):
        a_sum = 0.0
        for item in self.a_lst:
            a_sum = a_sum + float(item)
        return a_sum
    
    # Another function that will calculate the mean for values in a list
    def calc_mean(self):
        div = self.sum_my_lst()
        mean = float(div) / (len(self.a_lst))
        return mean
    
    def calc_median(self):        
        # sorts user input from highest to lowest using ".sort()" function
        lst_of_num.sort()          
    
        # Calculates median if list is even length
        if len(lst_of_num) % 2 == 0:
            first_mid = len(lst_of_num) / 2
            sec_mid = lst_of_num[int(first_mid)]
            numerator = float(first_mid) + float(sec_mid)
            median = numerator / len(lst_of_num)
            return median
        
        # Calculates median if list is odd length
        else:
            even_var = (len(lst_of_num) - 1) / 2
            median = lst_of_num[int(even_var)]
            return median

    def calc_mode(self):
        dct_of_nums = dict()
        
        for num in self.a_lst:
            if num not in dct_of_nums:
                dct_of_nums[num] = 1
            else:
                dct_of_nums[num] += 1
        
        mode = [val for val, key in dct_of_nums.items() if key > 1]
        return mode
    
    def standard_deviation(self):
        # Empty list for difference values
        diff_lst = []
        # Calculate mean of list
        sd_m = Calculator(self.a_lst)
        sd_mean = sd_m.calc_mean()
    
        # This goes through user inputed values and subtracts the the mean from
        # each value and then squares it. 
        for num in self.a_lst:
            result = ((float(num) - sd_mean) ** 2.0)
            # Then rounds the result to two digits
            rounded_result = round(result, 2)
            # Add these values to our difference values list
            diff_lst.append(rounded_result)
        # Here we take the mean of the differences
        new_calc = Calculator(diff_lst)
        new_sum = new_calc.calc_mean()        
        # Take the square root of that mean and we have our 
        #standard deviation
        standard_dev = (new_sum ** (1/2.0))
        return standard_dev
      
    def calc_range(self):
        # sorted_lst_range = lst_of_num.sort() 
        lst_of_num.sort()        
        max_var = lst_of_num[-1]
        min_var = lst_of_num[0]
        data_range = float(max_var) - float(min_var)
        return data_range

# An empty list where it adds the user input
lst_of_num = []     

print("Enter data points one by one, then type done. This calculator will calculate mean, median, mode, range and standard deviation. ")

# The original string is empty, causing the prompt to loop until
# the user enters 'done'. Stores the input as floats.
prompt = ""
while prompt != "done":
    prompt = input("Give me your data: ")
    if str(prompt.strip()) == "done" : break
    try:
        lst_of_num.append(float(prompt))
    except ValueError:
        print("Please enter an integer or a float.")
        print()

# Creates Calculator object to be used in rest of program.
usr_input = Calculator(lst_of_num)

print("\n")
print("You entered {} numbers".format(len(lst_of_num)))
print("The mean is: {}".format(str(usr_input.calc_mean())))
print("The median is: {}".format(str(usr_input.calc_median())))
print("The mode is: {}".format(str(usr_input.calc_mode()).strip("[]")))
print("The range is: {}".format(str(usr_input.calc_range())))
print("The standard deviation is: {}".format(str(usr_input.standard_deviation())))
print("Have a wonderful day!")
