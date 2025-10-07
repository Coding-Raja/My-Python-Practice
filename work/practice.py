#-----------------------------------------------------------------------
#------------------ Decorators in Python --------------------------------

def changecase(func):           # This is the DECORATOR function
  def myinner():               # This is the WRAPPER function
    return func().upper()      # Calls original function and converts to uppercase
  return myinner               # Returns the wrapper function

@changecase                    # This is DECORATOR SYNTAX
def myfunction():              # This is the ORIGINAL function
  return "\nHello Sally"

print(myfunction())


"""
What happens when you call myfunction():


The decorator has replaced myfunction with myinner

When you call myfunction(), you're actually calling myinner()

myinner() calls the original myfunction() and applies .upper()
"""