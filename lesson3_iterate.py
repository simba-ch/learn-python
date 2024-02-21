from collections.abc import Iterable
print(isinstance('abc',Iterable))
print(isinstance([0,1,2,3],Iterable))
print(isinstance(123,Iterable))

def findMinAndMax(L):
  min = None
  max = None
  for num in L:
    if min == None:
      min = num
    if max == None:
      max = num
  
    if not min == None and num < min:
      min = num
    elif not max == None and num > max:
      max = num
  return (min,max)