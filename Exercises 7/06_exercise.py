# Grupa m dzieci bawi się w układanie możliwie jak największej wieży. Każde dziecko ma
# klocki różnej wysokości. Pierwsze dziecko ma klocki o wysokościach w1, ..., wn, drugie
# dziecko klocki o wyskościach w1', ..., wn', itd. Dzieci właśnie poszły zjeść deser zanim
# ułożą swoje wieże, ale jedno dziecko zostało. Ma teraz jedyną okazję, żeby podebrać
# kilka klocków innym dzieciom tak, żeby jego wieża była najwyższa. Proszę podać algorytm
# rozwiązujący ten problem, który zabiera minimalną ilość klocków.


def build_tower(T):
    summary = []
    for i in range(len(T)):
        T[i].sort()
        summary.append(sum(T[i]))
    count = tower_height = idx = 0
    while tower_height < max(summary):
        maximum = 0
        for i in range(len(T)):
            if len(T[i]) != 0:
                if T[i][-1] > maximum:
                    maximum = T[i][-1]
                    idx = i
        height = T[idx].pop()
        tower_height += height
        summary[idx] -= height
        count += 1
    return count


bricks = [[16, 1, 30, 9, 12], [36, 47, 8, 19, 1, 72], [6, 38, 22, 31, 37]]
print(build_tower(bricks))
