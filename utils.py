import os

#custom print function
def printbb(incoming, clear_console=False):
  if clear_console == True:
    clear = lambda: os.system('clear')
    clear()
  print(incoming)

