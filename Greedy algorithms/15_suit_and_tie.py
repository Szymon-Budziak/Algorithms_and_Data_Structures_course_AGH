# Allen is hosting a formal dinner party. 2n people come to the event in n pairs (couples). After
# a night of fun, Allen wants to line everyone up for a final picture. The 2n people line up, but
# Allen doesn't like the ordering. Allen prefers if each pair occupies adjacent positions in the line,
# as this makes the picture more aesthetic. Help Allen find the minimum number of swaps of adjacent
# positions he must perform to make it so that each couple occupies adjacent positions in the line.


def suit_and_tie(n, T):
    swaps = 0
    for i in range(0, len(T), 2):
        for j in range(i + 1, len(T)):
            if T[i] == T[j]:
                index = j
                while T[i] != T[i + 1]:
                    T[index], T[index - 1] = T[index - 1], T[index]
                    index -= 1
                    swaps += 1
    return swaps


n = 8
T = [7, 6, 2, 1, 4, 3, 3, 7, 2, 6, 5, 1, 8, 5, 8, 4]
print(suit_and_tie(n, T))
