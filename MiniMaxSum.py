# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr_sorted = sorted(arr)
    min_sum = sum(arr_sorted[:-1])
    max_sum = sum(arr_sorted[1:])
    print(min_sum, max_sum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)