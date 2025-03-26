"""
Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or list or is null, return an empty array.
Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

using list comprehension:

def count_positives_sum_negatives(arr):
    return [sum(1 for x in arr if x > 0), sum(x for x in arr if x < 0)] if arr else []

"""

def count_positives_sum_negatives(arr):
    if arr is None or len(arr) == 0:
        return []
    count = 0
    sum_neg = 0
    for i in arr:
        count += 1 if i > 0 else 0
        sum_neg += i if i < 0 else 0
    return [count, sum_neg]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
