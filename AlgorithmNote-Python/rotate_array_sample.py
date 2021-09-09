# 정사각행렬
def rotate(arr):
    size = len(arr)
    result = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            result[j][size-1-i] = arr[i][j]

    return result


# 행과 열 길이가 다른 배열
def rotate_matrix(arr):
    row_len = len(arr)
    col_len = len(arr[0])
    result = [[0] * row_len for _ in range(col_len)]

    for r in range(row_len):
        for c in range(col_len):
            result[c][row_len-1-r] = arr[r][c]

    return result
