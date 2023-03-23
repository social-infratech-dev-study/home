array = list(map(int, input().split()))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pv = arr[len(arr) // 2]
    less, equal, greater = [], [], []
    for n in arr:
        if n < pv:
            greater.append(n)
        elif n > pv:
            less.append(n)
        else:
            equal.append(n)
    return quick_sort(less) + equal + quick_sort(greater)

print(quick_sort(array))