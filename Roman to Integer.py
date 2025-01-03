class Solution:
    def romanToInt(self, s: str) -> int: 
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}  # dictionary for roman numerals
        num = 0 # initialize num to 0
        for i in range(len(s)): # iterate through the string
            if i > 0 and roman[s[i]] > roman[s[i - 1]]: 
                # if the current value is greater than the previous value, subtract the previous value from the current value

                num += roman[s[i]] - 2 * roman[s[i - 1]] # subtract 2 times the previous value from the current value and add it to num
            else: # if the current value is less than or equal to the previous value
                num += roman[s[i]] # add the current value to num
        return num # return the final value of num