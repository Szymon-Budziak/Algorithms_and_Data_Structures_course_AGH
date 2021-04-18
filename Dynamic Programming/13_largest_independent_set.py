# Given a Binary Tree. Each node in this tree has the number of fun
# for each employee on event. Find the maximum number of fun in this set.
# This tree has to be independent set. A subset of all tree nodes is an
# independent set if there is no edge between any two nodes of the subset.


class Employee:
    def __init__(self, fun):
        self.fun = fun
        self.emp = []
        self.f = -1
        self.g = -1


def f(v):
    if v.f >= 0:
        return v.f
    x = v.fun
    for u in v.emp:
        x += g(u)
    y = g(v)
    v.f = max(x, y)
    return v.f


def g(v):
    if v.g >= 0:
        return v.g
    v.g = 0
    for u in v.emp:
        v.g += f(u)
    return v.g


root = Employee(7)
left = Employee(3)
bottom = Employee(5)
right = Employee(100)
root.emp.append(left)
root.emp.append(bottom)
root.emp.append(right)

left_left = Employee(13)
left_right = Employee(17)
left.emp.append(left_left)
left.emp.append(left_right)

bottom_bottom = Employee(19)
bottom.emp.append(bottom_bottom)

right_left = Employee(23)
right_right = Employee(29)
right.emp.append(right_left)
right.emp.append(right_right)
print(f(root))
