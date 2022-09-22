
# approach 1 - using list
# approach 2 - using hashmap
class OrderedStream:

    def __init__(self, n):
        self.values = [None] * n  # initialize an array of size n
        self.ptr = 0  # remeber where the stream pointer is at

    def insert(self, idKey, value):

        # set the arr's 0-indexed value to the incoming value
        self.values[idKey-1] = value

        # Construct the next chunk by checking bounds, and ensuring value is not None
        chunk = []
        while self.ptr < len(self.values) and self.values[self.ptr]:
            chunk.append(self.values[self.ptr])
            self.ptr += 1  # update the pointer

        return chunk


class OrderedStream:

    def __init__(self, n):
        self.ptr = 1
        self.hashmap = {}

    def insert(self, idKey, value):
        self.hashmap[idKey] = value
        output = []
        if idKey > self.ptr:
            return output

        while idKey in self.hashmap:
            output.append(self.hashmap[idKey])
            # del self.hashmap[idKey]  # To save some memory.
            idKey += 1
            self.ptr = idKey

        return output
