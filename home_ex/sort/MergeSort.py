def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key
    return arr


def merge_sort_non_increasing(arr):
    if len(arr) <= 1:
        return arr
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i >= 0 and arr[i] < key:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key
    return arr


def test():
    arr = [5, 2, 4, 6, 1, 3]
    print(merge_sort(arr))
    print(merge_sort_non_increasing(arr))


if __name__ == '__main__':
    test()
