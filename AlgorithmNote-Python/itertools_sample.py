import itertools

data = ['A', 'B', 'C']

# n개의 데이터를 뽑아 일렬로 나열하는 모든 경우 (순열)
print(list(itertools.permutations(data, 3)))

# n개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우 (조합)
print(list(itertools.combinations(data, 2)))

# 중복을 포함하는 순열
print(list(itertools.product(data, repeat=2)))

# 중복을 포함하는 조합
print(list(itertools.combinations_with_replacement(data, 2)))
