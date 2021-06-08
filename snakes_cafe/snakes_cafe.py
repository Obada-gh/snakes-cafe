print("""
$ python snakes_cafe.py
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
oneOrder=""
orders=[]

while oneOrder != 'quit':
  oneOrder = input('>')
  if oneOrder != 'quit':
    orders.append(oneOrder)
    i=orders.count(oneOrder)
    print(f'**{i} order of {oneOrder} added to your meal**')

