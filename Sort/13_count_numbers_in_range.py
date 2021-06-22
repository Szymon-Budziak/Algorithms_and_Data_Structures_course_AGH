# Find the class representing the data structure which in the constructor (__init__) gets an array of
# natural numbers of length n with the range of values [0, k]. It has to have a method
# count_numbers_in_range(a,b). It is supposed to return how many numbers in the range [a, b] were in
# the array. It is supposed to have O(1) time complexity. It can be assumed that always a >= 1, b <= k.


class Structure:
    def __init__(self, T):
        k = max(T)
        self.count = [0] * (k + 1)
        for i in range(len(T)):
            self.count[T[i]] += 1
        for i in range(1, k):
            self.count[i] += self.count[i - 1]

    def count_numbers_in_range(self, a, b):
        if a == 0:
            return self.count[b]
        else:
            return self.count[b] - self.count[a]


T = [5, 6, 2, 6, 87, 3, 78, 3, 23, 9, 67, 3, 5, 87, 1, 78, 2, 6, 1, 578, 26, 32, 18, 19, 31,
     52, 77, 48, 564, 42, 87, 234, 987, 325, 123, 874, 3, 1, 9, 456, 76, 34, 21, 34, 17, 5]
structure = Structure(T)
print(structure.count_numbers_in_range(1, 9))
