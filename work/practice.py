#-----------------------------------------------------------------------------

# ----------- Match Statement in Python -----------

x = int(input("\nEnter a number : "))

match x:
    case 0 : 
        print("\nIt is 0")
    case 1 : 
        print("\nIt is 1")
    case 2 : 
        print("\nIt is 2")
    case 3 : 
        print("\nIt is 3")
    case _ : 
        print("\nIt is greater than 3")            