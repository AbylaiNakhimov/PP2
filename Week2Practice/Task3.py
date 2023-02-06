s = input("string = ")
list1 = []
list2 = []
cnt1 = 0
cnt2 = 0
for i in s:
  if i == '':
    continue
  if i in list1:
    cnt1 += 1
  else:
    for j in s:
      if i == j:
        cnt2 += 1
    list1.append(i)
    list2.append(cnt2)
    cnt2 = 0
for i in range(len(list1)):
  print(list1[i], list2[i], sep = "->")