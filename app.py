
# first  change-1
from calc_func import do_addition , do_substraction


def main():
    print("Welcome to the calculator app")

    print("""\nSlect the function from  tr given options
          
          1. Add 
          2. Substract
          
          """)
    user_input = input("Select the function") 

    a = int(input("value of A"))
    b = int(input ("value of B"))

     
    if user_input == "1":

        result = do_addition(a,b)
 
    elif user_input == "2":

        result = do_substraction(a,b)

    print('Result:' , result)



if __name__ == "__main__":
    main()


        




