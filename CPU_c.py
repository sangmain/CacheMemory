class CPU:
    
    def __init__(self):
        self.alu = 0
        self.r1 = 0
        self.r2 = 0

    def process(self):
        self.alu = self.r1 + self.r2