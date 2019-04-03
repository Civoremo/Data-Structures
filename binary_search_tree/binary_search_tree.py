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
    print(f'self: {self.value} target: {target}')
    if self.value is None:
      return False
    else:
      if self.value == target:
        print(f'FOUND TARGET')
        return True
      else:
        if self.value > target:
          if self.left is not None:
            self.left.contains(target)
        else:
          if self.right is not None:
            self.right.contains(target)

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
    pass