from typing import Dict, List

COINS = [50, 25, 10, 5, 2, 1]

# Жадібний алгоритм
def find_coins_greedy(amount: int, coins: List[int]= COINS) -> Dict[int, int]:
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

# Динамічне програмування
def find_min_coins(amount: int, coins: List[int] = COINS) -> Dict[int, int]:
    dp = [0] + [float("inf")] * amount
    last_coin = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    # Відновлюємо результат
    result = {}
    i = amount
    while i > 0:
        coin = last_coin[i]
        result[coin] = result.get(coin, 0) + 1
        i -= coin

    return result

if __name__ == "__main__":
    # Приклад з нормальним набором монет
    amount = 113
    print("=== Набір монет [50,25,10,5,2,1] ===")
    print("Greedy:", find_coins_greedy(amount))
    print("DP:", find_min_coins(amount))

    # Приклад з "поганим" набором монет
    COINS_BAD = [9, 6, 1]

    def find_coins_greedy_bad(amount: int, coins: List[int] = COINS_BAD) -> Dict[int, int]:
        result = {}
        for coin in coins:
            if amount >= coin:
                count = amount // coin
                result[coin] = count
                amount -= coin * count
        return result

    def find_min_coins_bad(amount: int, coins: List[int] = COINS_BAD) -> Dict[int, int]:
        dp = [0] + [float("inf")] * amount
        last_coin = [0] * (amount + 1)

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    last_coin[i] = coin

        result = {}
        i = amount
        while i > 0:
            coin = last_coin[i]
            result[coin] = result.get(coin, 0) + 1
            i -= coin
        return result

    amount_bad = 12
    print("\n=== Набір монет [9,6,1], сума =", amount_bad, "===")
    print("Greedy:", find_coins_greedy_bad(amount_bad))
    print("DP:", find_min_coins_bad(amount_bad))
