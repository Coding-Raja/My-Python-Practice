#-----------------------------------------------------------------------
#------------------ Python *args and **kwargs --------------------------------

""" *args program 1
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
"""

""" *args program 2
def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))
"""