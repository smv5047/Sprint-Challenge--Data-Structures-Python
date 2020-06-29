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
            if self.buffer_pointer < self.capacity-1:
                self.buffer_pointer += 1
            else:
                self.buffer_pointer = 0
            return

    def get(self):
        return self.storage


new_buffer = RingBuffer(5)
new_buffer.append(1)
new_buffer.append(2)
new_buffer.append(3)
new_buffer.append(4)
new_buffer.append(5)
new_buffer.append(6)
new_buffer.append(7)
new_buffer.append(8)
new_buffer.append(9)
print(new_buffer.buffer_pointer)
new_buffer.append(45)
print(new_buffer.buffer_pointer)
# new_buffer.append(46)
# new_buffer.append(47)
# new_buffer.append(48)
# new_buffer.append(49)

# new_buffer.append('b')
print(new_buffer.get())
