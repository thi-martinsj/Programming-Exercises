import os


def diagonalDifference(arr, n):
    index_l = n
    index_r = 0
    left_sum = 0
    right_sum = 0
    
    while index_l >= 0:
        left_sum += arr[index_l][index_l]
        right_sum += arr[index_l][index_r]
        
        index_l -= 1
        index_r += 1
    
    return abs(left_sum - right_sum)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, (n-1))

    fptr.write(str(result) + '\n')

    fptr.close()
