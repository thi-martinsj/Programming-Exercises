import os


def getTotalX(a, b):
    total_x = 0

    start_point = max(a)
    endpoint = min(b)

    if start_point > endpoint:
        return 0

    for i in range(start_point, (endpoint + 1)):
        if all(i % x == 0 for x in a) and all(y % i == 0 for y in b):
            total_x += 1
    
    return total_x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
