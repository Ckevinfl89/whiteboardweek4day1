# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2


#determine all the consecutive one's(1) given in a list of [1 and 0s]

def solution(nums):
    running_number = 0
    max_count = 0
    for num in nums:
        if num == 1:
            running_number += 1
        else: 
           max_count.append(running_number)
           running_number = 0
    return(nums)
        
        


# def solution(nums):
#   max_count = 0
#   current_count = 0
#   for num in nums:
#     if num == 1:
#       current_count += 1
#       max_count = max(max_count, current_count)
#     else:
#       current_count = 0

#   return max_count