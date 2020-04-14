def mymax(xs):
  if not isinstance(xs, (list, tuple, set)):
    raise ValueError("unsupported type: " + str(type(xs)))
  elif len(xs) == 0:
    raise ValueError("max of empty is undefined")
  else:
    best = xs[0]
    for i in range(1, len(xs)):
      if best < xs[i]:
        best = xs[i]
    return best

# mymax(7)
