def descending_order(num):
    # Bust a move right here
    arr = list(str(num))
    l = len(arr)

    if l > 2:
        def recursive(arr):
            for i in range(1, l):
                if int(arr[i]) > int(arr[i-1]):
                    arr[i-1], arr[i] = arr[i], arr[i-1]
                    recursive(arr)
            return arr
        recursive(arr)
    elif l == 2:
        if int(arr[1]) > int(arr[0]):
            arr[0], arr[1] = arr[1], arr[0]
    else:
        return num

    return int(''.join(arr))


if __name__ == '__main__':
    print(descending_order(123456))
    print(descending_order(899818767))
