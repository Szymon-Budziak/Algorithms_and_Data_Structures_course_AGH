# A single digit is one that is exactly once in a given number. A multiple digit is one that is
# more than once in a given number. Natural number A is prettier than the natural number B
# if there are more single digits in A than in B, and if there are the same number of single
# digits, prettier number is one with fewer multiple digits. For example: 123 is prettier than
# 456, 1266 is prettier than 114577 and numbers 2344 and 67333 are equally pretty. We are given
# an array T with natural numbers. Find algorithm pretty_sort(T) that sorts the elements of an
# array T from the prettiest to the least pretty.


def convert_number(number):
    actual_number = number
    digits = [0] * 10
    while number > 0:
        digits[number % 10] += 1
        number //= 10
    single = multiple = 0
    for i in range(10):
        if digits[i] == 1:
            single += 1
        elif digits[i] > 1:
            multiple += 1
    return actual_number, single, multiple


def counting_sort(T, idx):
    count = [0] * 10
    result = [0] * len(T)
    for i in range(len(T)):
        count[T[i][idx]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    j = len(T) - 1
    while j >= 0:
        result[count[T[j][idx]] - 1] = T[j]
        count[T[j][idx]] -= 1
        j -= 1
    for i in range(len(T)):
        T[i] = result[i]
    T.reverse()


def pretty_sort(T):
    for i in range(len(T)):
        T[i] = convert_number(T[i])
    single_index = 1
    multiple_index = 2
    counting_sort(T, multiple_index)
    counting_sort(T, single_index)
    for i in range(len(T)):
        T[i] = T[i][0]
    return T


T = [455, 123, 1266, 114577, 2344, 67333]
print(pretty_sort(T))
