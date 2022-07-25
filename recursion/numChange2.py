def makeChange(coins_list, change, min_coins):
    for cents in range(change + 1):
        coin_count = cents
        for j in [c for c in coins_list if c <= cents]:
            # print(f'cc={coin_count} cents={cents} j={j} min_coins={min_coins}')
            if min_coins[cents-j] + 1 < coin_count:
                coin_count = min_coins[cents-j] + 1
        min_coins[cents] = coin_count
        print(min_coins)
    return min_coins[change]


if __name__ == "__main__":
    print(makeChange([1, 5, 10, 21, 25], 63, [0]*64))
