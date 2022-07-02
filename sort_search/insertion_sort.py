arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def insertionSort(arr):
    for i in range(0, 4):
        current_value = arr[i]
        position = i
        print(f'curr_v={current_value} pos={position}')
        while position > 0 and arr[position - 1] > current_value:
            print(f'curr_v{current_value} pos={position}')
            arr[position] = arr[position - 1]
            position = position - 1

        arr[position] = current_value

    return arr


print(insertionSort(arr))
