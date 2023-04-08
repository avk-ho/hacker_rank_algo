# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

import random

def birthday_cake_candles(candles):
    candles_heights = {}
    for candle_height in candles:
        candles_heights[candle_height] = candles_heights.get(candle_height, 0) + 1
    
    return candles_heights[max(candles_heights)]


def birthday_cake_candles2(candles):
    max_height = 0
    max_num = 0
    for candle_height in candles:
        if candle_height > max_height:
            max_height = candle_height
            max_num = 1
            
        elif max_height == candle_height:
            max_num += 1
    
    return max_num


# candles = [4, 4, 1, 2]
nb_candles = 10
max_height = 5
candles = [random.randint(1, max_height) for _ in range(nb_candles)]
print(candles)
print(birthday_cake_candles(candles))
print(birthday_cake_candles2(candles))