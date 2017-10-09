def array_left_rotation(a, n, k):
    """Left array rotation
    
    https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
    :param a: input array
    :param n: array length
    :param k: the number of left rotations you must perform
    :return: 
    """
    return [
        y[1] for y in
        sorted(
            [((i+(n-k)) % n, a[i])
                for i in range(n) ],
            key=lambda x: x[0]
        )
    ]

if __name__=='__main__':
    input_1 = "5 4"
    input_2 = "1 2 3 4 5"

    n, k = map(int, input_1.strip().split(' '))
    a = list(map(int, input_2.strip().split(' ')))
    answer = array_left_rotation(a, n, k)
    print(*answer, sep=' ')