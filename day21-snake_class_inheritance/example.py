# to inherit from another class, do the following below:

class Animal:
  def __init__(self):
    self.num_eyes = 2

  def breathe(self):
    print("Inhale, exhale")

class Fish(Animal):
  def __init__(self):
      super().__init__()

  def breathe(self):
    super().breathe() #calls the breathe method in the super class
    print("doing this underwater")

  def swim(self):
    print("Gluck gluck, i am swimming")

nemo = Fish()
nemo.swim()
nemo.breathe()


# slicing function
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[2:]) # returns everything from the 2nd index in an array
print(piano_keys[:5]) # returns everything before the 5th index in an array
print(piano_keys[2:6]) #returns everything from the 2nd index, to right before the 6th index
print(piano_keys[2:6:2]) #returns the values from above, except it increments after every other item