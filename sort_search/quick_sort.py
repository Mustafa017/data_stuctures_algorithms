arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def quicksort(arr):
    recursive_partitioner(arr, 0, len(arr)-1)
    return arr


def recursive_partitioner(arr, first, last):
    if first < last:
        split_point = partitioner(arr, first, last)

        # left half of arr before split_point
        recursive_partitioner(arr, first, split_point-1)

        # Right half of arr after split_point
        recursive_partitioner(arr, split_point+1, last)


def partitioner(arr, first, last):
    # print(f'{arr} {first} {last}')
    pivot = arr[first]
    leftmark = first+1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and arr[leftmark] <= pivot:
            leftmark += 1

        while arr[rightmark] >= pivot and rightmark >= leftmark:
            rightmark -= 1

        if(rightmark < leftmark):
            done = True
            # print(
            #     f'leftmark={leftmark}, rightmark={rightmark} done={done}')
        else:
            # print(
            #     f'leftmark={leftmark}, rightmark={rightmark} done={done}')
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]

    arr[first], arr[rightmark] = arr[rightmark], arr[first]

    return rightmark


print(quicksort(arr))
