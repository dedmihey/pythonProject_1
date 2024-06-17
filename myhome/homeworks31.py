class EvenNumbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        if self.start % 2 == 0:
            self.i = self.start
        else:
            self.i = self.start + 1
        return self

    def __next__(self):
        global n
        if self.i <= self.end:
            n = self.i
            self.i += 2
            return n
        else:
            raise StopIteration


en = EvenNumbers(20, 40)
print(en)
for j in en:
    print(j)
