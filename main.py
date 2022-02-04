#from dogclass import dogs

class dogs:

  def __init__(self, name, breed, age, color):
    self.name = name
    self.breed = breed
    self.age = age
    self.color = color
  
  '''def __str__(self):
    return 'dogs(name = '+str(self.name)+', breed = '+str(self.breed)+', age = '+str(self.age)+', color = '+str(self.color)+')'''

dog1 = dogs('sam','retriever', '8', 'yellow')
dog2 = dogs('jim','shiba',13,'tan')

print(dogs.__str__(dog1))
print(dogs.__str__(dog2))
