#-----------------------------------------------------------------------
#------------------ Decorators in Python --------------------------------
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "\nHello " + nam

print(myfunction("Raja"))