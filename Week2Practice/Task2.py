x = input()
i = 0
while i < len(x) / 2:
  if x[i] != x[len(x) - i - 1]:
    print("false")
  else:
    print("true")
  break
    
