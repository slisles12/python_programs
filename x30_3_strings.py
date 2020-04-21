
def repeat_until(s, n=100):
    """ Repeats s until the string is n characters long.
        The last part of the returned string will be
        the appropriate prefix of s to give a result with length n
    """
    
    res = s
    while len(res) < n:
        res = res + s
    return res[0:n]
    
    
if __name__ == "__main__":
   
   print(repeat_until("hi", 100))