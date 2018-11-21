# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 21:16:04 2018

@author: Robert Barclay
"""
"""
    This a simple calculator that calculates the mean, median, range, mode, and standard deviation to five
    decimal points. It prompts the user to enter in their data one by one, then it asks for what the user 
    wants to calculate. The program then calculates the all five and prints it to the console. 
    
    Attributes:
        Calculator class: This class has a method that sums the list passed in which is used by the other 
        five methods calc_mean, calc_median, standard_deviation, calc_range and calc_mode. These methods calculate 
        the mean, the median, the standard deviation, the range and the mode based on the numbers provided by the 
        user.
        
"""
class Calculator:
    def __init__(self, _a_lst):
        self._a_lst = _a_lst
    
    #A simple function that sums the values in the list. I added this instead of
    #the 'sum' function to practice coding.
    def sum_my_lst(self):
        a_sum = 0.0
        for item in self._a_lst:
            a_sum = a_sum + float(item)
        return a_sum
    
    # Another function that will calculate the mean for values in a list
    def calc_mean(self):
        div = self.sum_my_lst()
        mean = float(div) / (len(self._a_lst))
        return mean
    
    def calc_median(self):        
        # sorts user input from lowest to highest using ".sort()" function
        lst_of_num.sort()    
        # Calculates median if list is even length
        if len(lst_of_num) % 2 == 0:
            # Computest the 'middle' of an even list by finding half of the length
            # and subracting by one due to the zero index nature of lists in Python
            index = int((len(lst_of_num) - 1) / 2)
            # Sets variable 
            first_num = lst_of_num[index]
            sec_num = lst_of_num[index + 1]
            lst_sum = float(first_num) + float(sec_num)
            even_median = lst_sum / 2
            return even_median
        
        # Calculates median if list is odd length
        else:
            lst_middle = (len(lst_of_num) - 1) / 2
            odd_median = lst_of_num[int(lst_middle)]
            return odd_median

    def calc_mode(self):
        dct_of_nums = dict()
        for num in self._a_lst:
            if num not in dct_of_nums:
                dct_of_nums[num] = 1
            else:
                dct_of_nums[num] += 1
        
        # Check if all the sum of valuesin the dictionary equal the length of the
        # data input by the user. If not it returns the mode, else returns a 
        # message saying no mode found. 
        mode = dict((key, val) for key, val in dct_of_nums.items() if val > 1)
        if len(mode) >= 1:
            return mode
        else:
            return ('No value appeared more than once.')
    
    def standard_deviation(self):
        # Empty list for difference values
        diff_lst = []
        # Calculate mean of list
        sd_m = Calculator(self._a_lst)
        sd_mean = sd_m.calc_mean()
    
        # This goes through user inputed values and subtracts the the mean from
        # each value and then squares it. 
        for num in self._a_lst:
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


if __name__ == '__main__':
	# An empty list where it adds the user input
	lst_of_num = []     

	print("This calculator will calculate mean, median, mode, range and standard deviation. Enter data points one by one, then type 'done'.")

	# The original string is empty, causing the prompt to loop until
	# the user enters 'done'. Stores the input as floats.
	prompt = ""
	while prompt != "done":
		prompt = input("Enter your data: ")
		if str(prompt.strip()) == "done" : break
		try:
			lst_of_num.append(float(prompt))
		except ValueError:
			print("Please enter an integer or a decimal.")

# Attempts to create a Calculator object and calculate based on user entered data
try:
    usr_input = Calculator(lst_of_num)    
    print("\n")
    print("You entered {} numbers".format(len(lst_of_num)))
    print("The mean is: {}".format(str(round(usr_input.calc_mean(), 5))))
    print("The median is: {}".format(str(round(usr_input.calc_median(), 5))))
    mode_vals = usr_input.calc_mode()
    if type(mode_vals) is not str:
        print("Mode: These numbers were entered this many times: ")
        for key in mode_vals:
            print("{}: {}".format(int(key), mode_vals[key]))
    else:
        print("Mode: " + mode_vals)
    #print("The mode is: {}".format(str(usr_input.calc_mode())))
    print("The range is: {}".format(str(usr_input.calc_range())))
    print("The standard deviation, (sigma) is: {}".format(str(round(usr_input.standard_deviation(), 5))))
    print("Have a wonderful day!")

except ZeroDivisionError:
    print('Please try again with integers or decimals.')
