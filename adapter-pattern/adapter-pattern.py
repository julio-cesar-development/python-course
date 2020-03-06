"""
Convert the interface of a class into another interface clients expect.
Adapter lets classes work together that couldn't otherwise because of
incompatible interfaces.
"""

import abc


class Target(metaclass=abc. ABCMeta):
  """
  Define the domain-specific interface that Client uses.
  """

  def __init__(self):
    print('__init__ Target')
    self._adaptee = Adaptee()

  @abc.abstractmethod
  def request(self):
    print('request => Target')
    pass


class Adapter(Target):
  """
  Adapt the interface of Adaptee to the Target interface.
  """

  def __init__(self):
    super().__init__()
    print('__init__ Adapter')

  def request(self):
    print('request => Adapter')
    self._adaptee.custom_request()


class Adaptee:
  """
  Define an existing interface that needs adapting.
  """

  def __init__(self):
    print('__init__ Adaptee')

  def custom_request(self):
    print('custom_request => Adaptee')
    pass


def main():
  adapter = Adapter()
  adapter.request()


if __name__ == "__main__":
  main()
