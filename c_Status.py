

class Status:

    def __init__(self, is_allcache=True):
        
        self.is_hit = []
        self.hit_cnt = 0
        self.hit_rate = 0.0

        self.data_location1 = None
        self.data_location2 = None
        
        self.access_time = []
        self.average_time = 0.0

        if is_allcache:
            self.time_dict = {2: 0.3, 3: 0.3, 4: 0.3, 5: 1.3, 6: 4.3} #### access time
            self.cache_index = [2, 3, 4]

        else:
            self.time_dict = {2: 0.3, 3: 1.3, 4: 4.3} #### access time
            self.cache_index = [2]
                        
    
    def set_location(self, storage_key):
        self.is_hit.append(storage_key in self.cache_index)
        self.access_time.append(self.time_dict[storage_key])
        # if self.data_location1 is None:
        #     self.data_location1 = storage_key

        # else:
        #     self.data_location2 = storage_key

    def end(self, loop_size):
        self.hit_cnt = sum(self.is_hit)
        self.hit_rate = self.hit_cnt / (loop_size * 2)
        self.average_time = sum(self.access_time) / (loop_size * 2) 