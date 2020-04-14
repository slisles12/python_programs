import math

def is_prime(x):
    """ Returns True if x is prime
        x must be >= 2
    """
    
    if x <= 1:
        raise ValueError("Must be greater than 1")
    bound = int(math.sqrt(x))

    for i in range(2, bound+1):
        if x % i == 0:
            return False
        return True


    
# Use "python x30_1_primes.py" to run the file
# Use "python -i 01_primes.py" to run the file, then jump into interpreter
# Use "quit()" to exit interpreter

# Commands for when I run this as a script
if __name__ == "__main__":
    
   while True:
        theInput = input("type a number or ENTER to quit: ")
        if not theInput: # if len(theInput == 0)
            break
        try:
            x = int(theInput)
            if is_prime(x):
                print(str(x) + " is prime")
            else:
                print(str(x) + " is not prime")
        except ValueError:
            print("Invalid")