from abc import ABC, abstractmethod

# classe base abstrata
class Bebida(ABC):
  def __init__(self):
    self.descricao = ''

  # non abstract
  def get_descricao(self):
    return self.descricao

  @abstractmethod
  def get_preco(self):
    pass


# classe concreta
class Expresso(Bebida):
  def __init__(self):
    print('__init__ Expresso')
    self.descricao = 'Café Expresso'

  def get_preco(self):
    return 1.50


# classe abstrata decorator
class DecoratorBebida(Bebida):
  def __init__(self, __bebida):
    print('__init__ DecoratorBebida')
    self.bebida = __bebida

  @abstractmethod
  def get_descricao(self):
    pass


# classes decoradora
class Moca(DecoratorBebida):
  def __init__(self, __bebida):
    print('__init__ Moca')
    self.bebida = __bebida
    super().__init__(__bebida)

  # non abstract
  def get_descricao(self):
    return self.bebida.get_descricao() + ' Moca'

  # non abstract
  def get_preco(self):
    return self.bebida.get_preco() + 0.25


class Creme(DecoratorBebida):
  def __init__(self, __bebida):
    print('__init__ Creme')
    self.bebida = __bebida
    super().__init__(__bebida)

  # non abstract
  def get_descricao(self):
    return self.bebida.get_descricao() + ' Creme'

  # non abstract
  def get_preco(self):
    return self.bebida.get_preco() + 0.75


# classe cliente
class Cafeteria:
  def __init__(self):
    expresso = Expresso()
    print(expresso.get_descricao() + ' :: R$ ' + str(expresso.get_preco()))

    moca = Moca(expresso)
    print(moca.get_descricao() + ' :: R$ ' + str(moca.get_preco()))

    creme = Creme(moca)
    print(creme.get_descricao() + ' :: R$ ' + str(creme.get_preco()))


def main():
  # intancia a classe cliente
  Cafeteria()


if __name__ == "__main__":
  main()
