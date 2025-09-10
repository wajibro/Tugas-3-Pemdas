x = {3,4,5,2,1,10,8,77,60,50}
maks = 0
# For Loop
for i in x:
  if x[i] > x[i-1]:
    if x[i] > maks:
      maks = x[i]
  elif x[i] < x[i-1]:
    if x[i-1] > maks:
      maks = x[i-1]
  else:
    continue

print(maks)