A = int(input("a = "))
B = int(input("b = "))
C = int(input("c = "))
counterInit = 0
def getProps(a, b, c, cntr, func):
    counter = cntr
    A = a + 1
    if(A%c==0 and a != b):
      print(A)
      counter+=1
      func(A,b,c,counter)
    elif(A == b - 1):
      print("\n{} multiple number".format(counter))
    else:
      func(A,b,c,counter)
def getMultiple(a,b,c,cntr):
    getProps(b,a,c,cntr,getMultiple) if a > b else getProps(a,b,c,cntr,getMultiple)
getMultiple(A,B,C,counterInit)