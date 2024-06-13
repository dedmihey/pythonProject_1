class EvenNumbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = self.start
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.start:
            if self.i > self.end:
                raise StopIteration
            if self.i % 2 == 0:
                self.start = self.i
        return self.start


en = EvenNumbers(20, 40)
print(en)
for j in en:
    print(j)
