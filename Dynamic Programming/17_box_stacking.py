# Given set of #D boxes, where each box has height, width and length. We have
# unlimited supply fo these boxes. Find the maximum height of boxes placement that
# the going on the top should have strictly less length and width than the box on
# which it is going. Also print how to place the boxes on top of each other to get
# this maximum height.


def possible_rotations(box, rotations):
    i = box[0]
    j = box[1]
    k = box[2]
    rotations.append((max(i, j), min(i, j), k))
    rotations.append((max(i, k), min(i, k), j))
    rotations.append((max(j, k), min(j, k), i))


def print_solution(result, rotations):
    i = len(result)-1
    while i != -1:
        print(rotations[i])
        i = result[i]


def box_stacking(boxes):
    rotations = []
    for i in range(len(boxes)):
        possible_rotations(boxes[i], rotations)
    rotations.sort(key=lambda x: x[0]*x[1])
    rotations.reverse()
    max_height = [-1]*len(rotations)
    result = [0]*len(rotations)
    for i in range(len(max_height)):
        max_height[i] = rotations[i][2]
    for i in range(len(result)):
        result[i] = i
    result[0] = -1
    j = 0
    i = 1
    while j < len(max_height)-1:
        if i == j:
            j = 0
            i += 1
        elif rotations[i][0] < rotations[j][0] \
                and rotations[i][1] < rotations[j][1]:
            height = max_height[j] + rotations[i][2]
            if height > max_height[i]:
                max_height[i] = height
                result[i] = j
            j += 1
        else:
            j += 1
    print_solution(result, rotations)
    return max_height[-1]


boxes = [(1, 2, 4), (3, 2, 5), (3, 4, 9), (3, 2, 7)]
# (height, width, length)
print(box_stacking(boxes))
