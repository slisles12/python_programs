""" A list of items formed by repeating some sequence several times """
class RepeatedList:
  def __init__(self, xs, reps):
    """ Build a list from repeating xs reps times
        Example: for xs = ["a", 2, 10] and reps = 2,
        then self should be "a", 2, 10, "a", 2, 10
    """
    self.base = xs
    self.reps = reps
  
  def __len__(self):
    """ Returns the number of items in the repeated list """
    # TODO: complete this method
    
    
  # "overloads" the [] operator
  def __getitem__(self, index):
    if index >= 0 and index < len(self):
      return # TODO: determine the value to return
    else:
      raise ValueError("Index " + str(index) + " out of bounds")