import bisect

'''
이진 탐색의 구현용 라이브러리
정렬된 배열에서 특정 원소를 찾아야 할 때 효과적
bisect_left : 정렬된 순서를 유지하면서 리스트에 값을 삽입할 가장 왼쪽 인덱스 반환
bisect_right : 정렬된 순서를 유지하면서 리스트에 값을 삽입할 가장 오른쪽 인덱스 반환
'''

data = [1, 2, 4, 4, 8]
x = 4

print(bisect.bisect_left(data, x))
print(bisect.bisect_right(data, x))

# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수 구하기


def count_by_range(arr, left_value, right_value):
    right_idx = bisect.bisect_right(arr, right_value)
    left_idx = bisect.bisect_left(arr, left_value)
    return right_idx - left_idx


a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터의 개수
print(count_by_range(a, 4, 4))

# 값이 -1, 3 범위에 있는 데이터 개수
print(count_by_range(a, -1, 3))
