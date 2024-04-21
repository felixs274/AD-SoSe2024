#
# In Zusammenarbeit zwischen Daniel Heisig, Felix Scholzen & Simon Wagner
#


example_list = [20, 8, 17, 3, 14, 9, 1, 12, 5, 18, 7, 15, 2, 11, 19, 6, 10, 4, 13, 16]


# Task 1.1
def insertion_sort(list):
    for i in range(len(list)):
        value = list[i]
        j = i - 1
        while (j >= 0) and (list[j] < value):
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = value


# Task 1.2
def bubble_sort(list):
    n = len(list)
    for i in range(n-1):
        for j in range(0, n-1):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j+1] = tmp





print(example_list)

insertion_sort(example_list)
print(example_list)

bubble_sort(example_list)
print(example_list)