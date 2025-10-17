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

#-------------- **kwargs -----------
"""
If you do not know how many keyword arguments will be passed into your function, 
add two asterisks ** before the parameter name.
**kwargs Example 1:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
"""
"""
Example 2:

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")
"""