counterInit = 0
A = int(input("a = "))
B = int(input("b = "))
C = int(input("c = "))
def getProps(a, b, c, cntr, func):
  counter = cntr
  A = a + 1
  (print(A),func(A,b,c,counter + 1)) if (A%c==0 and a != b and A!=0) else (print("\n{}".format(counter)) if A==b - 1 else func(A,b,c,counter))
def getMultiple(a,b,c,cntr):
  getProps(b,a,c,cntr,getMultiple) if a > b else getProps(a,b,c,cntr,getMultiple) if c != 1 else print("Invalid")
getMultiple(A,B,C,counterInit)