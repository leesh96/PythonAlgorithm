while True:
    # try:
    #     A, B = map(int, input().split())
    #     print(A + B)
    # except:
    #     break
    nums = list(map(int, input().split()))
    if nums:
        A, B = nums
        print(A + B)
    else:
        break
