# One day n friends met at a party, they hadn't seen each other for a long time and so they decided
# to make a group photo together. Simply speaking, the process of taking photos can be described as
# follows. On the photo, each photographed friend occupies a rectangle of pixels: the i-th of them
# occupies the rectangle of width w[i] pixels and height h[i] pixels. On the group photo everybody
# stands in a line, thus the minimum pixel size of the photo including all the photographed friends,
# is W x H, where W is the total sum of all widths and H is the maximum height of all the photographed
# friends. As is usually the case, the friends made n photos — the j-th (1 <= j <= n) photo had everybody
# except for the j-th friend as he was the photographer. Return the minimum size of each made photo
# in pixels. Return n numbers b1, b2, ..., bn where bi — the total number of pixels on the minimum
# photo containing all friends expect for the i-th one.


def photo_to_remember(T):
    heights = []
    total_width = 0
    for i in range(len(T)):
        total_width += T[i][0]
        heights.append(T[i][1])
    heights.sort()
    for i in range(len(T)):
        actual_width = total_width - T[i][0]
        actual_height = heights[-1]
        if actual_height == T[i][1]:
            actual_height = heights[-2]
        print(actual_width * actual_height)


T = [(3, 123), (1, 456), (2, 789)]
photo_to_remember(T)
