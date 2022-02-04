class dogs:

  def __init__(self, name, breed, age, color):
    self.name = name
    self.breed = breed
    self.age = age
    self.color = color
  
  def __str__(self):
    return 'dogs(name = '+str(self.name)+', breed = '+str(self.breed)+', age = '+str(self.age)+', color = '+str(self.color)+')'
