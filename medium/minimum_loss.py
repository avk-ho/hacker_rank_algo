# https://www.hackerrank.com/challenges/minimum-loss/problem?isFullScreen=true

import random

def minimum_loss(prices):
    def get_minimum_loss_for_year(idx):
        year_price = prices[idx]
        minimum_loss = None

        for price in prices[idx+1:]:
            loss = year_price - price

            if loss > 0:
                if minimum_loss is None \
                        or loss < minimum_loss:
                    minimum_loss = loss

        if minimum_loss is not None:
            minimum_loss_per_year.append(minimum_loss)

    minimum_loss_per_year = []

    i = 0
    while i < len(prices) - 1:
        get_minimum_loss_for_year(i)
        i += 1

    # print(minimum_loss_per_year)
    if len(minimum_loss_per_year) > 0:
        return min(minimum_loss_per_year)
    else:
        return -1


prices1 = [20, 15, 8, 2, 12]  # 15 - 12
prices2 = [5, 10, 3]  # 5 - 3
prices3 = [20, 7, 8, 2, 5]  # 7 - 5
prices4 = [1, 3]  # impossible

prices_len = random.randint(2, 10)
rand_prices = [random.randint(1, 20) for _ in range(prices_len)]
print(rand_prices)

print(minimum_loss(prices1))
print(minimum_loss(prices2))
print(minimum_loss(prices3))
print(minimum_loss(prices4))
print(minimum_loss(rand_prices))