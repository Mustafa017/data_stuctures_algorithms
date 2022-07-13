def makeChange(coins, n):
    min_coins = n
    if n in coins:
        return 1
    else:
        for i in [c for c in coins if c <= n]:
            numCoins = 1 + makeChange(coins, n-i)
            print('numCoins='+str(numCoins))
            if numCoins < min_coins:
                print('am here')
                min_coins = numCoins

    return min_coins


if __name__ == '__main__':
    print(makeChange([1, 5, 10, 25], 8))
