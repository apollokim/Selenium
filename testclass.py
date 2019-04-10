class a():
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

count =a('4',5)
print(count.add())