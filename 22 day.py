def firstOne(get):
    left, right = 0, 1  
    while get(right) == 0:
        left = right
        right *= 2

    while left < right:
        mid = left + (right - left) // 2
        if get(mid) == 1:
            right = mid
        else:
            left = mid + 1
    return left
