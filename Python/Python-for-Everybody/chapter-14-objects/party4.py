# Object Lifecycle
# (see https://books.trinket.io/pfe/14-objects.html)

class PartyAnimal:
   x = 0

   def __init__(self):
     print('I am constructed')

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self):
     print('I am destructed', self.x)

an = PartyAnimal()
an.party()
an.party()
an = 42
print('an contains',an)

# Code: http://www.py4e.com/code3/party4.py


# When this program executes, it produces the following output:
# I am constructed
# So far 1
# So far 2
# I am destructed 2
# an contains 42