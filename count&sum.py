# Return an array, where the first element is the count of positives numbers
# and the second element is sum of negative numbers.


def count_positives_sum_negatives(arr):
    if len(arr) == 0:
       res = []
       return res
    res = [0, 0]
    for i in arr:
        if i > 0:
            res[0] += 1
        else:
            res[1] += i
    return res