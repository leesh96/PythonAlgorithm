word = input().lower()
ch_list = list(set(word))
cnt_list = []

for ch in ch_list:
    cnt_list.append(word.count(ch))

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    print(ch_list[cnt_list.index(max(cnt_list))].upper())
