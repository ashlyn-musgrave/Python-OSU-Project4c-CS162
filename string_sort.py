# Author: Ashlyn Musgrave
# GitHub Username: ashlyn-musgrave
# Date: 7/16/2023
# Description: This program modifies insertion sort to sort a list of strings instead of numbers

def insertion_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos].lower() > value.lower():
      a_list[pos + 1] = a_list[pos]
      pos -= 1
    a_list[pos + 1] = value