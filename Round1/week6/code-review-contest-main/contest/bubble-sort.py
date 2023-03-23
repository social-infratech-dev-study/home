print("오름차순으로 정렬할 값을 입력해주세요. 값들은 빈칸으로 구분해주세요.")

array = list(map(int, input().split()))

def bubble_sort(arr):
    n = len(arr)
    for j in range(n - 1):
        for i in range(n - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return array

print(bubble_sort(array))