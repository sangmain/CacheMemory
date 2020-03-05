import pickle

with open("./Result/LRU/64hit.txt", 'rb') as f:
    is_hit = pickle.load(f)
with open("./Result/LRU/64time.txt", 'rb') as f:
    access_time = pickle.load(f)
print(is_hit[])