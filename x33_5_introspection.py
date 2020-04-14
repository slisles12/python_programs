def info(object, collapse=True):
    """Print methods and doc strings.
    Takes module, class, list, dictionary, or string."""
    
    # TODO: What types are in methodList?
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    
    # TODO: What kind of thing is processDoc?
    processDoc = (lambda s: " ".join(s.split())) if collapse else (lambda s: s)
    
    # TODO: What is longestMethod (i.e., a plain-language description)?
    longestMethod = max([ len(x) for x in methodList ])
    
    # s.ljust(x) will return a string where s is left-justified
    #   in a string of length x
    # TODO: What does getattr(object, methodName) return?
    lines = [methodName.ljust(longestMethod) + " " + processDoc(str(getattr(object, methodName).__doc__))
               for methodName in methodList ]
    print("\n".join(lines))

if __name__ == "__main__":
    print (info.__doc__)

# Adapted from http://www.diveintopython.net/power_of_introspection/index.html    
# Added parens for print (to adapt from Python 2.x)
# Changed and-or trick to conditional expression (for processFunc assignment)
# Removed the "spacing" argument and hard-coded it

