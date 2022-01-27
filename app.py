import addition as a
import division as d
import multiplication as m
import subtraction as s

choice = input("Please enter choice (1: Addition, 2: Subtraction, 3: Multiplication or 4: Division ")


try:
    num1 = int(input ("Please enter the first number: "))
except TypeError as e:
    print("Can't figure out how to do those!")
except ValueError as e:
    print('You must enter and actual number!')
    print(e)
except:
    print("Sorry something went wrong")


try:
    num2 = int(input ("Please enter the second number: "))
except TypeError as e:
    print("Can't figure out how to do those!")
except ValueError as e:
    print('You must enter and actual number!')
    print(e)
except:
    print("Sorry something went wrong")

   
    
if choice == '1':    
    try:
        x = print(num1, " + ", num2, " = ", a.addition(num1, num2))
    except TypeError as e:
        print("Can't figure out how to do those!")
    except ValueError as e:
        print('You must enter and actual number!')
        print(e)
    except:
        print("Sorry something went wrong")
   
elif choice == '2':    
    try:
        x = print(num1, " - ", num2, " = ", s.subtraction(num1, num2))
    except TypeError as e:
        print("Can't figure out how to do those!")
    except ValueError as e:
        print('You must enter and actual number!')
        print(e)
    except:
        print("Sorry something went wrong")    

elif choice == '3':    
    try:
        x = print(num1, " * ", num2, " = ", m.multiply(num1, num2))
    except TypeError as e:
        print("Can't figure out how to do those!")
    except ValueError as e:
        print('You must enter and actual number!')
        print(e)
    except:
        print("Sorry something went wrong") 
       
elif choice == '4':    
    try:
        x = print(num1, " / ", num2, " = ", d.division(num1, num2))
    except ZeroDivisionError as e:
        print("Can't Divide By Zero!")
    except TypeError as e:
        print("Can't figure out how to do those!")
    except ValueError as e:
        print('You must enter and actual number!')
        print(e)
    except:
        print("Sorry something went wrong")     

else:    
   print("Your input is invalid")  

