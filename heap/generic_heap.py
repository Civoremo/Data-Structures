class Heap:
  def __init__(self, comparator):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    # pass
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    # pass
    removed = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return removed

  def get_max(self):
    # pass
    return self.storage[0]

  def get_size(self):
    # pass
    return len(self.storage)

  def _bubble_up(self, index):
    # pass
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        temp = self.storage[index]
        self.storage[index] = self.storage[(index - 1) // 2]
        self.storage[(index - 1) // 2] = temp
      index = (index - 1) // 2

  def _sift_down(self, index):
    # pass
    while (index * 2) + 1 <= len(self.storage) - 1:
      if (index * 2) + 2 > len(self.storage) - 1:
        largest = (index * 2) + 1
      else:
        if self.storage[(index * 2) + 1] > self.storage[(index * 2) + 2]:
          largest = (index * 2) + 1
        else:
          largest = (index * 2) + 2
      if self.storage[index] < self.storage[largest]:
        temp = self.storage[index]
        self.storage[index] = self.storage[largest]
        self.storage[largest] = temp
      index = largest