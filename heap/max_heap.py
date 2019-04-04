class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    # pass
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    # pass
    # temp storage of item that we are deleting
    removed = self.storage[0]
    # replace item we are deleting with last item in array
    self.storage[0] = self.storage[len(self.storage) - 1]
    # remove last item in array
    self.storage.pop()
    # move first item down tree to correct position
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
    # while left.index is >= 0
    while (index - 1) // 2 >= 0:
      # if left.index.value < current.index.value
      if self.storage[(index - 1) // 2] < self.storage[index]:
        # switch the values of left.index and current.index
        temp = self.storage[index]
        self.storage[index] = self.storage[(index - 1) // 2]
        self.storage[(index - 1) // 2] = temp
      # update current index with left.index
      index = (index - 1) // 2

  def _sift_down(self, index):
    # pass
    # while left.index <= last.index
    while (index * 2) + 1 <= len(self.storage) - 1:
      # if right.index > last.index
      if (index * 2) + 2 > len(self.storage) - 1:
        # set largest_child = left.index
        largest = (index * 2) + 1
      else:
        # if left.index.value > right.index.value
        if self.storage[(index * 2) + 1] > self.storage[(index * 2) + 2]:
          # largest_child.index = left.index
          largest = (index * 2) + 1
        else:
          # largest_child.index = right.index
          largest = (index * 2) + 2
      # if current.index.value < largest_child.Index.value
      if self.storage[index] < self.storage[largest]:
        # switch the values of current.index with largest_child.index
        temp = self.storage[index]
        self.storage[index] = self.storage[largest]
        self.storage[largest] = temp
      # set current.index to largest_child.index
      index = largest