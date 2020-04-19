def logText(text: str) -> None:
  print(text + ' STRING')

def uppercaseText(text: str) -> str:
  return text.upper()

text = 'text'

logText(text)

text = uppercaseText(text)

print(text)

def printListItems(listParam: list) -> None:
  print([str(item).lower() for item in listParam])

lista = ((text + ' ') * 3).split(' ')
# lista.pop(len(lista) - 1)
lista = list(filter(lambda x: x != '', lista))
print(lista)

printListItems(lista)
