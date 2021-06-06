print('**************************************')
print('**    Welcome to the Snakes Cafe!   **')
print('**    Please see our menu below.    **')
print('**')
print('** To quit at any time, type "quit" **')
print('**************************************')
print('\nAppetizers\n----------\nWings\nCookies\nSpring Rolls')
print('\nEntrees\n-------\nSalmon\nSteak\nMeat Tornado\nA Literal Garden')
print('\nDesserts\n--------\nIce Cream\nCake\nPie')
print('\nDrinks\n------\nCoffee\nTea\nUnicorn Tears')
print('\n***********************************\n** What would you like to order? **\n***********************************')
i=1
while i< 999999:
  userOrder = input('>')
  
  if userOrder == 'quit':
      break
  print(f'** {i} order of {userOrder} have been added to your meal **')  
  i+=1