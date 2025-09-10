x = [3,4,5,2,1,10,8,77,60,50]
j = 0
maks = 0

# for Loop
for i in range( len(x)):
  if x[i] > maks:
    maks = x[i]
  else:
    continue

print(maks)
maks = 0

# while Loop
while j < len(x):
  if x[j] > maks:
    maks = x[j]
  j += 1

print(maks)