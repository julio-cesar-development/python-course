# () = tuplas, são imutáveis
# [] = listas
# {} = dicionarios

lanche = 'Hamburguer', 'Pizza', 'Café', 'Suco'
# lanche = ('Hamburguer', 'Pizza', 'Café', 'Suco')

print(lanche) # ('Hamburguer', 'Pizza', 'Café', 'Suco')
print(sorted(lanche)) # ['Café', 'Hamburguer', 'Pizza', 'Suco']

print(lanche[0]) # 'Hamburguer'

print(lanche[0:2]) # ('Hamburguer', 'Pizza')

print(lanche[2:]) # ('Café', 'Suco')

print(lanche[:2]) # ('Hamburguer', 'Pizza')

print(lanche[-1]) # 'Suco'

print(len(lanche)) # 4

print("\n")

# iteração pelos elementos
for item in lanche:
  # os 3 seguintes modos de print terão o mesmo resultado
  # print("Item %s"%(item))
  # print(f'Item {item}')
  print('Item {}'.format(item))
# Item Hamburguer
# Item Pizza
# Item Café
# Item Suco

print("\n")

# iteração com index
for idx in range(len(lanche)):
  print('Item {}'.format(lanche[idx]))
# Item Hamburguer
# Item Pizza
# Item Café
# Item Suco

print("\n")

# iteração com enumerate
for idx, item in enumerate(lanche):
  # print('Item {}'.format(lanche[idx]))
  print('Item {}'.format(item))
# Item Hamburguer
# Item Pizza
# Item Café
# Item Suco

print("\n")

lanche2 = lanche + lanche

print(lanche2) # ('Hamburguer', 'Pizza', 'Café', 'Suco', 'Hamburguer', 'Pizza', 'Café', 'Suco')

print(lanche2.count('Hamburguer')) # 2

print(lanche2.index('Hamburguer')) # 0

print("\n")

del lanche2 # apagar a tupla

print("End")
