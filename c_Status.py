

class Status:

    def __init__(self, storage_len):
        
        self.is_hit = []
        self.hit_cnt = 0
        self.hit_rate = 0.0

        self.data_location1 = None
        self.data_location2 = None
        
        self.access_time = []
        self.average_time = 0.0

        if storage_len == 3:
            self.time_dict = {2: 0.1, 3: 10, 4:300} #### access time
            self.cache_index = [2]
        elif storage_len == 4:
            self.time_dict = {2: 0.1, 3: 0.3, 4: 10, 5: 300} #### access time
            self.cache_index = [2, 3]
        else:
            self.time_dict = {2: 0.1, 3: 0.3, 4: 0.7, 5: 10, 6: 300} #### access time
            self.cache_index = [2, 3, 4]
    
    def set_location(self, storage_key):
        self.is_hit.append(storage_key in self.cache_index)
        self.access_time.append(self.time_dict[storage_key])
        # if self.data_location1 is None:
        #     self.data_location1 = storage_key

        # else:
        #     self.data_location2 = storage_key

    def end(self, loop_size):
        self.hit_cnt = sum(self.is_hit)
        self.hit_rate = self.hit_cnt / loop_size
        self.average_time = sum(self.access_time) / loop_size