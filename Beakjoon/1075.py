n = int(input())
f = int(input())

front = n // 100
end = front * 100

while True:
    if end % f == 0:
        break
    end += 1

end = str(end)
print(end[-2:])
