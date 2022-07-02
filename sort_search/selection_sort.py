from turtle import position


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def selection_sort(arr):
    l = len(arr)-1
    for slot in range(l, 0, -1):
        max_pos = 0
        for idx in range(1, slot+1):
            if arr[idx] > arr[max_pos]:
                max_pos = idx

        arr[idx], arr[max_pos] = arr[max_pos], arr[idx]
    return arr


print(selection_sort(arr))
