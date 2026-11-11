# Welcome message
print (" Welcome , everyone , to the GitHub tutorial !")
def introduction_task () :
    print ("\n- - - Python Task ---")
    print ("Let ’s write a function that adds two numbers !")
def add_numbers (a , b ) :
    return a + b
num1 = 5
num2 = 7
result = add_numbers ( num1 , num2 )
print ( f"{ num1 } + { num2 } = { result }")
print (f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2:.2f}")
else: 
    print("cannot divide by zero")
print(f"The larger number:{max(num1, num2)}")
introduction_task ()
print("Welcome to our Git tutorial")