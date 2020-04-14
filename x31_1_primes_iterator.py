
class PrimeNumbers:
    """ An iterator that produces the first n prime numbers """
    
    def __init__(self, n=100):
        """ n is the number of prime numbers to generate """        
        self.n = n
        

    
    # Starting method name with __ makes it private    
    def __is_prime(self, x):
        """ Preconditions: x is a positive integer greater than self.primes[-1] """
        
        # TODO: complete this with the instructor
    
    
    
    def __append_next_prime(self):    
        """ Precondition: self.primes is not empty 
            Places the next prime in the list self.primes """

        # TODO: complete this with the instructor
  
        
        
    def __iter__(self):
        # self.primes contains the primes we have found so far,
        #  which is nothing for a new iterator
        self.primes = []
        return self
        
        
    def __next__(self):
        # TODO: complete this with the instructor
        
        