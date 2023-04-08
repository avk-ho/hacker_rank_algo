import random

def birthday_cake_candles(candles):
    candles_heights = {}
    for candle_height in candles:
        candles_heights[candle_height] = candles_heights.get(candle_height, 0) + 1
    
    return candles_heights[max(candles_heights)]


# candles = [4, 4, 1, 2]
nb_candles = 10
max_height = 5
candles = [random.randint(1, max_height) for _ in range(nb_candles)]
print(candles)
print(birthday_cake_candles(candles))