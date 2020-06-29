class RingBuffer:

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.buffer_pointer = 0

    def append(self, item):
        # Is buffer at capacity?
        if len(self.storage) < self.capacity:
            self.storage.insert(len(self.storage), item)
            return
        else:
            self.storage[self.buffer_pointer] = item
            if self.buffer_pointer < self.capacity:
                self.buffer_pointer += 1
            else:
                self.buffer_pointer = 0
            return

    def get(self):
        return self.storage


new_buffer = RingBuffer(5)
new_buffer.append('a')
new_buffer.append('b')
new_buffer.append('c')
new_buffer.append('d')
new_buffer.append('e')
# new_buffer.append('b')
print(new_buffer.get())
