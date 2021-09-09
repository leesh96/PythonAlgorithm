array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


# 선택 정렬
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        # 스왑
        arr[i], arr[min_index] = arr[min_index], arr[i]


# 삽입 정렬
def insertion_sort(arr):
    for i in range(1, len(arr)):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break


# 퀵 정렬
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    tail = arr[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# 계수 정렬
def count_sort(arr):
    count = [0] * (max(arr) + 1)

    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')
