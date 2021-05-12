# 순차 탐색
def sequential_search(n, target, arr):
    for i in range(n):
        if arr[i] == target:
            return i + 1


# 이진 탐색
def binary_search(arr, target, start, end):
    # 재귀적 표현
    # if start > end:
    #     return None
    # mid = (start + end) // 2
    #
    # if arr[mid] == target:
    #     return mid
    # elif arr[mid] > target:
    #     return binary_search(arr, target, start, mid - 1)
    # else:
    #     return binary_search(arr, target, mid + 1, end)

    # 반복문 사용
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


# bisect의 구현
def find_start(arr, key):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid
    return start


def find_end(arr, key):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid
        else:
            start = mid + 1
    return start
