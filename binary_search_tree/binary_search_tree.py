class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # pass
    if self.value is None:
      self = BinarySearchTree(value)
    else:
      if self.value <= value:
        if self.right is None:
          self.right = BinarySearchTree(value)
        else:
          return self.right.insert(value)
      elif self.value > value:
        if self.left is None:
          self.left = BinarySearchTree(value)
        else:
          return self.left.insert(value)

  def contains(self, target):
    # pass
    if self.value is None:
      return False
    else:
      if self.value == target:
        return True
      elif self.value > target:
        if self.left is not None:
          return self.left.contains(target)
      else:
        if self.right is not None:
          return self.right.contains(target)

  def get_max(self):
    # pass
    if self.value is None:
      return None
    max = self.value
    right = self.right
    while right is not None:
      max = right.value
      right = right.right
    return max

  def for_each(self, cb):
    # pass
    if self.value is None:
      cb(self.value)
    elif self.left is None and self.right is None:
      cb(self.value)

    if self.left is not None:
      self.left.for_each(cb)
      cb(self.value)
    if self.right is not None:
      self.right.for_each(cb)
      cb(self.value)