# We are given a safe that cna be unlocked with four-digit PIN (0000 - 9999). Below the
# display there are some buttons with numbers from 1 to 9999 (for example: 13, 223, 782, 3902).
# This safe works differently tha the normal one. Pressing a button with a number adds the
# number from a button to the number on the display. If sum is greater than 9999, the first
# number is cut. We know the PIN and the numbers that are currently displayed. Find the
# shortest button press sequence that will allow us to unlock the safe. If such a sequence
# doesn't exist, return None.
from queue import Queue


def count_digits(number):
    count = 0
    while number != 0:
        number //= 10
        count += 1
    return count


def safe(buttons, display, PIN):
    if display == PIN:
        return True
    T = [[] for _ in range(len(buttons))]
    visited = [False for _ in range(10000)]
    for i in range(len(buttons)):
        T[i] = buttons[i] + display
    queue = Queue()
    for i in range(len(buttons)):
        queue.put(T[i])
    while not queue.empty():
        actual_display = queue.get()
        if actual_display == PIN:
            return True
        for i in range(len(buttons)):
            temp_display = actual_display
            temp_display += buttons[i]
            if temp_display > 9999:
                digits = count_digits(temp_display)
                temp_display %= 10 * (digits)
            if not visited[temp_display]:
                visited[temp_display] = True
                queue.put(temp_display)
    return False


display = 1234
PIN = 7384
buttons = [13, 223, 782, 3902, 500]
print(safe(buttons, display, PIN))
