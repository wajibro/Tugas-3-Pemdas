x = [3,4,5,2,1,10,8,77,60,50]
i = 0
maks = 0

# for Loop
for i in range( len(x)):
  if x[i] > maks:
    maks = x[i]
  elif x[i-1] > maks:
    maks = x[i-1]
  else:
    continue
print(maks)
maks = 0

# while Loop
while i < len(x):
  if x[i] > maks:
    maks = x[i]
  elif x[i-1] > maks:
    maks = x[i-1]
  else:
    continue
print("cihuy")