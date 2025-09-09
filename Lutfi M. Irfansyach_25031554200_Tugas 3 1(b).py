counter = 0
while counter <= 100:
  print("///", counter, "////")
  if counter % 2:
    counter *= 2
    print("Ini elif 2 =", counter)
  else:
    counter += 1
    print("Ini elif 1 =", counter)