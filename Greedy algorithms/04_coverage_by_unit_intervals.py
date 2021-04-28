# Given set X of points on straight line. Find minimum number of closed unit intervals
# that are needed to cover all points from X.


def cover_points(X):
    X.sort()
    max_right = count = 0
    for i in range(len(X)):
        if X[i] > max_right:
            max_right = X[i]+1
            count += 1
    return count


X = [0.25, 0.5, 1.6, 1, 5, 2.3, 3.1, 4.5]
print(cover_points(X))
