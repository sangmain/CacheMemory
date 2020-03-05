import cache_random
import cache_fifo
import cache_lru

import pandas as pd
import multiprocessing as mp
if __name__ == '__main__':
    file = pd.read_csv("./Data/cc1.csv")
    length = len(file)
    mp.freeze_support()
    pool = mp.Pool(processes=mp.cpu_count())

    # cache_lru.start(file, length, 128, 8000)
    # cache_random.start(file, length, 128, 8000)
    # cache_fifo.start(file, length, 128, 8000)
    
    results = []
    param = (file, length, 64, 1000)
    result = pool.apply_async(cache_lru.start, param)
    results.append(result)
    result = pool.apply_async(cache_fifo.start, param)
    results.append(result)
    result = pool.apply_async(cache_random.start, param)
    results.append(result)

    param = (file, length, 64, 3000)
    result = pool.apply_async(cache_lru.start, param)
    results.append(result)
    result = pool.apply_async(cache_fifo.start, param)
    results.append(result)
    result = pool.apply_async(cache_random.start, param)
    results.append(result)

    param = (file, length, 64, 6000)
    result = pool.apply_async(cache_lru.start, param)
    results.append(result)
    result = pool.apply_async(cache_fifo.start, param)
    results.append(result)
    result = pool.apply_async(cache_random.start, param)
    results.append(result)

    param = (file, length, 64, 8000)
    result = pool.apply_async(cache_lru.start, param)
    results.append(result)
    result = pool.apply_async(cache_fifo.start, param)
    results.append(result)
    result = pool.apply_async(cache_random.start, param)
    results.append(result)

    param = (file, length, 64, 12000)
    result = pool.apply_async(cache_lru.start, param)
    results.append(result)
    result = pool.apply_async(cache_fifo.start, param)
    results.append(result)
    result = pool.apply_async(cache_random.start, param)
    results.append(result)

    for r in results:
        r.wait()



