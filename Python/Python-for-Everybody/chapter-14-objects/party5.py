# Many instances
# (see https://books.trinket.io/pfe/14-objects.html)

class PartyAnimal:
   x = 0
   name = ''
   def __init__(self, nam):
     self.name = nam
     print(self.name,'constructed')

   def party(self) :
     self.x = self.x + 1
     print(self.name,'party count',self.x)

s = PartyAnimal('Sally')
s.party()
j = PartyAnimal('Jim')
j.party()
s.party()

# Code: http://www.py4e.com/code3/party5.py

# The output of the program shows that each of the objects (s and j) contain their own 
# independent copies of x and nam:
# Sally constructed
# Sally party count 1
# Jim constructed
# Jim party count 1
# Sally party count 2
