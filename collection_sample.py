from collections import deque
from collections import Counter

'''
deque
파이썬의 스택, 큐 구현 라이브러리
양쪽에서의 삽입, 삭제 가능
스택 : append(), pop() 사용
큐 : append(), popleft() 사용
'''

Q = deque()

# 왼쪽 삽입
Q.appendleft(1)

# 오른쪽 삽입
Q.append(2)

# 왼쪽 삭제
Q.popleft()

# 오른쪽 삭제
Q.pop()

'''
Counter
iterable 객체가 해당 객체 내부의 원소가 몇 번씩 등장했는지를 알려준다.
'''

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['red'])
