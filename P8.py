"""
The four adjacent digits in the 1000-digit number that have the greatest product are
9 * 9 * 8 * 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
821663704844031**9989**0008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
"""


def getMax(num, maxStr, n, k):
    for i in range(n - k):
        if num[i] <= num[i + k]:
            maxStr = num[i + 1:i + k + 1]
        else:
            lastMax = getMax(num[i + 1:], maxStr, n - i - 1, k)
            # print num[i + 1:], lastMax, maxStr
            sum1 = 1
            sum2 = 1
            for char in lastMax:
                sum1 *= int(char)
            for char in maxStr:
                sum2 *= int(char)
            if sum1 >= sum2:
                maxStr = lastMax
            break
    return maxStr


def main():
    t = 1
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n, k = 10, 5
        n, k = raw_input().strip().split(' ')
        n, k = [int(n), int(k)]
        num = '3675356291'
        num = raw_input().strip()
        maxStr = num[0:k]
        temp = getMax(num, maxStr, n, k)
        sum1 = 1
        for char in temp:
            sum1 *= int(char)
        print sum1
    return 0


if __name__ == '__main__':
    # print "This program is being run by itself"
    main()
else:
    print 'I am being imported from another module'
