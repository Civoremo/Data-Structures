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
      if self.value < value:
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
    pass

  def get_max(self):
    pass

  def for_each(self, cb):
    pass