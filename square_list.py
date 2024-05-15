# Author: Jovane Cano
# GitHub username: jovanecano
# Date: 05/14/2024
# Description:
"""Inlcudes a fucntion named square_list that takes as a parameter a list of numbers and replaces each value
    with its square."""


def square_list(nums):
    """This function mutates the given list of values and replaces with its square"""
    for number in range(len(nums)):
        nums[number] = nums[number] ** 2  # **2 squares the ith value


# nums = [7, -3, 12, 9]
# square_list(nums)
# print(nums)
