# -*- coding: utf-8 -*-
str_list = ['a', 'b', 'c', 'd', '']

def func_handle(str_list):
  print('lista com strings não vazias => {}'.format(str_list))

if any(s == '' for s in str_list):
  print('Erro: strings vazias existem na lista!')
else:
  func_handle(str_list)

if all(s != '' for s in str_list):
  func_handle(str_list)
else:
  print('Erro: strings vazias existem na lista!')

if any(s != '' for s in str_list):
  func_handle(str_list)
else:
  print('Erro: strings vazias existem na lista!')

if all(['a' == 'a', 'b' == 'b']):
  print("all 'a' == 'a' && 'b' == 'b'")

if any(['a' == 'b', 'b' == 'a', 'a' == 'a']):
  print("any 'a' == 'b', 'b' == 'a', 'a' == 'a'")
