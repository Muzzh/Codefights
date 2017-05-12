def minimalNumberOfCoins(coins, price):
    num = 0
    for i in coins[::-1]:
        num += price/i
        price = price%i
    return num
