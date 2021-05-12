import heapq

'''
기본적으로 최소힙으로 구현 -> 오름차순 정렬
PriorityQueue 라이브러리보다 빠르다.
'''

# 힙 정렬


def heapsort(arr):
    temp = []
    result = []

    # 삽입
    for value in arr:
        heapq.heappush(temp, value)
    # 삭제 후 담기
    for i in range(len(temp)):
        result.append(heapq.heappop(temp))

    return result

