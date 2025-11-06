def selection_sort(arr):
    l = len(arr)
    for i in range(0, l):
        min = arr[i]
        swap_index = i
        for j in range(i+1, l):
            if arr[j] < min:
                min = arr[j]
                swap_index = j
        arr[swap_index] = arr[i]
        arr[i] = min
    return arr

def test():
    a = [31, 41, 59, 26, 41, 58]
    print(selection_sort(a))

if __name__ == '__main__':
    test()
