# We are given an array A of size n that is sorted in ascending order, containing different
# natural numbers in pairs. Find algorithm that checks if there is such an index i that A[i] == i.
# What will change if the numbers are integers, not necessarily natural numbers?


# Natural numbers


def is_index_equal_to_number_natural(T):
    if T[0] == 0:
        return True
    else:
        return False


# Integer numbers


def is_index_equal_to_number_integer(T):
    start = 0
    end = len(T) - 1
    while start <= end:
        mid = (start + end) // 2
        if T[mid] == mid:
            return True
        elif T[mid] > mid:
            end = mid - 1
        else:
            start = mid + 1
    return False


natural_numbers = [2, 4, 6, 7, 9, 11, 12, 15, 16, 37, 56, 87, 94, 98]
integer_numbers = [-10, -6, -4, -1, 2, 5, 12, 23, 34, 54, 57, 67, 79]
print(is_index_equal_to_number_natural(natural_numbers))
print(is_index_equal_to_number_integer(integer_numbers))
