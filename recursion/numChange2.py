def makeChange(coins_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count = cents
        newCoin = 1
        for j in [c for c in coins_list if c <= cents]:
            if min_coins[cents-j] + 1 < coin_count:
                coin_count = min_coins[cents-j] + 1
                newCoin = j
        min_coins[cents] = coin_count
        coins_used[cents] = newCoin
    printCoins(coins_used, change)
    # print(coins_used[change])
    return min_coins[change]


def printCoins(coinsUsed, change):
    coins = change
    while coins > 0:
        thisCoin = coinsUsed[coins]
        print(thisCoin)
        coins = coins - thisCoin


if __name__ == "__main__":
    print(makeChange([1, 5, 10, 21, 25], 63, [0]*64, [0]*64))
