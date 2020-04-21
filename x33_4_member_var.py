
def member_var(obj, prop):
    if prop in dir(obj): 
        return getattr(obj, prop)
    else:
        return None

x = 7
print(member_var(x, "real"))      
print(member_var(x, "not_here"))    