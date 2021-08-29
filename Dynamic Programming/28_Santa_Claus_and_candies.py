# Santa Claus has n candies, he dreams to give them as gifts to children. What is the maximal number
# of children for whose he can give candies if Santa Claus want each kid should get distinct positive
# integer number of candies. Santa Class wants to give all n candies he has.
# Return number k - maximal number of kids which can get candies and k distinct integer numbers: number
# of candies for each of k kid. The sum of k printed numbers should be exactly n. If there are many
# solutions, print any of them.


def santa_claus_and_candies(n):
    result = []
    i = 1
    while n > 0:
        if n - i >= 0:
            result.append(i)
            n -= i
            i += 1
        else:
            result[-1] += n
            break
    return len(result), result


n = 7
print(santa_claus_and_candies(n))
