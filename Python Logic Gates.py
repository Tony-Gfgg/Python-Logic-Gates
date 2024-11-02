def gate_not(a):
 if a == 0:
  a += 1
  print(a)
 elif a == 1:
  a -= 1
  print(a)

def gate_and(a, b, c):
 if a == 1 and b == 1:
  c = 1
  print(c)
 else:
  c = 0
  print(c)



gate_and(0, 1, 0)
gate_not(1)