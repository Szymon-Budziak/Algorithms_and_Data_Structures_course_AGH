# Given set of loads = [w1, w2, ..., wn] and maximum capacity K of trail. Weight
# of each load is the power of two. Find algorithm that chooses such loads that
# the trailer is possibly most loaded. Also we used as less loads as it is possible
# to load the trail.


def loading_K(weights, K):
    weights.sort(reverse=True)
    count = 0
    result = K
    for i in range(len(weights)):
        if weights[i] <= result:
            count += 1
            result -= weights[i]
    return count


weights = [2, 2, 4, 8, 1, 8, 16]
K = 27
print(loading_K(weights, K))
