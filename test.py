class asd:
    def __init__(self):
        self.a = 10
    def __call__(self):
        print("call")

    def __getitem__(self, item):
        print("aaaa")
        return self.a

    def __customaa__(self):
        print("bbb")

    def __

a = asd()

b = a