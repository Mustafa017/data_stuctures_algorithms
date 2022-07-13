def makeChange(coins, n, knownResults):
    min_coins = n
    if n in coins:
        knownResults[n] = 1
        return 1
    elif knownResults[n] > 0:
        return knownResults[n]
    else:
        for i in [c for c in coins if c <= n]:
            numCoins = 1 + makeChange(coins, n-i, knownResults)
            print('numCoins='+str(numCoins))
            if numCoins < min_coins:
                print('am here')
                min_coins = numCoins
            knownResults[n] = min_coins

    return min_coins


if __name__ == '__main__':
    print(makeChange([1, 5, 10, 25], 63, [0]*64))
