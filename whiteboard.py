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
    max_count = []
    for num in nums:
        if num == 1:
            running_number += 1
        else: 
           max_count.append(running_number)
           running_number = 0
    max_count.append(running_number)
    return max(max_count)
        


def solution(nums):
    consecutive_nums = 0
    max_consecutive = 0
    for num in nums:
        if num:
            consecutive_nums += 1
        else:
            if consecutive_nums > max_consecutive:
                max_consecutive = consecutive_nums
            consecutive_nums = 0
    if consecutive_nums > max_consecutive:
        max_consecutive = consecutive_nums
    return max_consecutive



def solution(nums):
    return max(map(len, ''.join(map(str, nums)).split('0')))
        


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


def solution(num_list):
    num_count = 0 # Iterate over each number and if its a 1 add to count
    consecutive_ones = []
    for num in num_list:
        if num == 1:
            num_count += 1
            consecutive_ones.append(num_count)
        else:
            consecutive_ones.append(num_count)
            num_count = 0

    return max(consecutive_ones)