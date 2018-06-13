import sys
from itertools import product
import time
sys.setrecursionlimit(100)


def list_to_num(n, base):
    x = n[0]
    for number in n[1:]:
        x *= base
        x += number
    return x


def get_possible_moves(process_list, n):
    possible_change = []
    if process_list[0] == process_list[-1]:
        possible_change.append([0, (process_list[0] + 1) % (n+1)])
    for ind in range(1, n):
        if process_list[ind] != process_list[ind - 1]:
            possible_change.append([ind, process_list[ind - 1]])
    return possible_change


def mutual_exclusion(process_list, n):
    global pomoc
    state = list_to_num(process_list, n)
    if pomoc[state] != -1:
        return pomoc[state]
    possible_change = get_possible_moves(process_list, n)
    if len(possible_change) == 1:
        pomoc[state] = 0
        return 0
    max_value = 0
    for index, value in possible_change:
        new_process_list = process_list.copy()
        new_process_list[index] = value
        current_value = mutual_exclusion(new_process_list, n) + 1
        if current_value > max_value:
            max_value = current_value
            pomoc[state] = max_value
    return max_value


# 5 -> 24, 6 -> 38, 7 -> 55, 8 -> 75, 9 -> 98
# 7348.919718503952
# 98


k = 4
pomoc = [-1] * (k+1)**k
s = time.time()
for i, el in enumerate(product(range(k), repeat=k)):
    mutual_exclusion(list(el), k)
print(time.time() - s)
print(max(pomoc))


test