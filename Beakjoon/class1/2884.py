H, M = map(int, input().split())
clock = H*60 + M
new_alarm = clock - 45
if new_alarm < 0:
    new_alarm += 23*60 + 60
print(new_alarm // 60, new_alarm % 60)