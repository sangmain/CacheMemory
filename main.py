import cache_random
import cache_fifo
import cache_lru

import pandas as pd

file = pd.read_csv("./Data/cc1.csv")
length = 1000
cache_lru.start(file, length, 64, 1000, 200)
cache_random.start(file, length, 64, 1000, 200)
cache_fifo.start(file, length, 64, 1000, 200)

