a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
counter = 0
def getMultiple(a,b,c,cntr):
  counter = cntr
  if(a > b):
    B = b + 1
    if(B%c==0 and B != a):
      print(B)
      counter+=1
      getMultiple(a,B,c,counter)
    elif(B == a):
      print("\n{} multiple number".format(counter))
    else:
      getMultiple(a,B,c,counter)
  elif(a < b):
    A = a + 1
    if(A%c==0 and A != b):
      print(A)
      counter+=1
      getMultiple(A,b,c,counter)
    elif(A==b):
      print("\n{} multiple number".format(counter))
    else:
      getMultiple(A,b,c, counter)
  else: print("Invalid")
getMultiple(a,b,c,counter)