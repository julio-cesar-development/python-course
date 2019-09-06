class Transport:
  def __init__(self, name, weight, price):
    self.name = name
    self.weight = weight
    self.price = price

  def getName(self):
    return self.name

  def getWeight(self):
    return self.weight

  def getPrice(self):
    return self.price

trans1 = Transport('Fusca', 500, 3950.50)
print(trans1.getName())
print(trans1.getWeight())

# inheriting from Transport
class Car(Transport):
  def __init__(self, name, weight, price, additional_price):
    Transport.__init__(self, name, weight, price)
    self.additional_price = additional_price
    self.__additional_price_with_interest = price + (additional_price * 0.5) # private property

  def getAdditionalPrice(self):
    return self.additional_price

  # @property to 'getter' functions
  @property
  def additional_price_with_interest(self):
    return self.__additional_price_with_interest

  # @property.setter to 'setter' functions
  @additional_price_with_interest.setter
  def additional_price_with_interest(self, additional_price):
    self.__additional_price_with_interest = self.price + (additional_price * 0.5)

trans2 = Car('Fusca 2', 1000, 4450.50, 500)
print(trans2.getName())
print(trans2.getWeight())
print(trans2.getAdditionalPrice())

print(trans2.additional_price_with_interest)
trans2.additional_price_with_interest = 400
print(trans2.additional_price_with_interest)
