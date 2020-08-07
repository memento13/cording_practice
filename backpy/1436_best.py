from bisect import bisect

'''
    O(log(N)) solution.
    written by books1234
'''
def solution(N):
    # order must start at 0
    n = N - 1

    # find max digits
    f = [0, 0, 0, 1]
    D = 3
    while n >= f[D]:
        f.append(9*f[D]+9*f[D-1]+9*f[D-2]+10**(D-2))
        D += 1
    digits = [0] * (D+1)

    k = D
    count6 = 0
    lower, upper = (0, f[k])

    while k > 3 and count6 != 3:
        # partition by first digit (0~9) and 10-ary tree search
        partition = [lower+i*f[k-1] for i in range(0,7)] \
                    + [upper-(10-i)*f[k-1] for i in range(7,11)]
        digit = bisect(partition, n) - 1
        digits[k] = digit
        lower, upper = partition[digit], partition[digit+1]

        # count if current digit is 6
        count6 = count6+1 if digit == 6 else 0
        k -= 1
    
    # fill additional 6 if needed
    digits[k-(2-count6):k+1] = [6] * (3-count6)

    # string to number and add remainder
    answer = int(''.join(map(str, reversed(digits[1:])))) + n - lower
    return answer

n = int(input().strip())
print(solution(n))