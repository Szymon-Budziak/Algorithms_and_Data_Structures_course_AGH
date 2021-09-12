# Hash table implementation


class Node:
    def __init__(self, key, value, state):
        self.key = key
        self.value = value
        self.state = state


class HashTable:
    def __init__(self, length):
        self.length = length
        self.array = [None] * length


def hash_t(table, key):
    length = table.length
    return hash(key) % length


"""
1st implementation:

This implementation is not using Node class. This implementation is based only on HashTable class.
"""


def add(table, key, value):
    index = hash_t(table, key)
    if table.array[index] is not None:
        for i in table.array[index]:
            if i[0] == key:
                i[1] = value
                break
            else:
                table.array[index].append([key, value])
    else:
        table.array[index] = []
        table.array[index].append([key, value])


def get(table, key):
    index = hash_t(table, key)
    if table.array[index] is None:
        return None
    else:
        for i in range(table.length):
            if table.array[i][0] == key:
                return table.array[i][1]
        return None


def print_hash_table(table):
    print("{", end="")
    for i in range(table.length):
        if table.array[i] is None:
            print(None, ":", None, end=", ")
        else:
            for j in table.array[i]:
                print(j[0], ":", j[1], end=", ")
    print("}")


hash_table = HashTable(7)
add(hash_table, 5, 19)
add(hash_table, 20, 4)
add(hash_table, 'b', 'bcd')
add(hash_table, 3, 'hello')
add(hash_table, 0, 6)
print_hash_table(hash_table)

"""
2nd implementation:

This implementation is using Node class and HashTable class.
"""


def find(table, key):
    index = hash_t(table, key)
    count = 1
    while table.array[index] is not None and count <= table.length:
        if table.array[index].key == key and table.array.state != 2:
            return index
        index = (index + 1) % table.length
        count += 1
    return None


def insert(table, key, value):
    index = hash_t(table, key)
    count = 1
    while table.array[index] is not None and table.array[index].state == 1 and count <= table.length:
        index = (index + 1) % table.length
        if key == 0:
            count += 1
    if count == table.length + 1:
        return None
    else:
        node = Node(key, value, 1)
        table.array[index] = node


def remove(table, key):
    index = hash_t(table, key)
    if index is None:
        print("no key", key)
    else:
        table.array[index].state = 2


def print_table(table):
    print("{", end="")
    for i in range(table.length):
        if table.array[i] is None:
            print(None, ":", None, end=", ")
        else:
            print(table.array[i].key, ":", table.array[i].value, end=", ")
    print("}")


h_table = HashTable(7)
insert(h_table, 5, 19)
insert(h_table, 20, 4)
insert(h_table, 'b', 'bcd')
insert(h_table, 3, 'hello')
insert(h_table, 0, 6)
print_table(h_table)
