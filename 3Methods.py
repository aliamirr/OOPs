class Counter:
    def __init__(self):
        self.count = 0
        self.locked = False

    def toggle_lock(self):
        self.locked = not self.locked
        # if self.locked == True:
        #     self.locked = False
        # else:
        #     self.locked = True

    def increment(self):
        if self.locked:
            raise Exception("The counter is locked!")
        self.count += 1

    def decrement(self):
        if self.locked:
            raise Exception("The counter is locked!")
        self.count -= 1

    def print_count(self):
        print(f"The current count is {self.count}")



counter = Counter()
# counter2 = Counter()


counter.increment()
counter.increment()
counter.increment()
counter.decrement()
counter.print_count()

counter.toggle_lock()
counter.decrement()
