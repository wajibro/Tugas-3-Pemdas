def flowchart():
  print("""
Isi dari array x = 3, 4, 5, 2, 1, 10, 8, 77, 60, 50

Flowchart pencarian data maks menggunakan for & while loop :

                            Atur nilai maks bernilai 0
                                      |
                                      |
                                      |
                                      V
                Periksa data array [x] dengan perulangan tiap [i] <-------------------> Semua x sudah di periksa
                                      |                                |                           |
                                      |                                |                           |
                                      |                                |                           |
                                      |                                |                           |
                                      V                                |                           |
                Apakah nilainya lebih besar dari variabel maks?        |                           |
                                      |                                |                           |
                                      |                                |                           |
                                      |                                |                           |
                                      V                                |                           |                  
                [Ya]<-------------------------------------->[Tidak]-----                           |
                  |                                         continue   A                           |
                  |                                                    |                           |
                  |                                                    |                           |
                  V                                                    |                           |
Simpan nilai tersebut kedalam variabel maks ----------------------------                           |
                                                                                                   |
                                                                                                   V
                                                                              Tampilkan nilai maks akhir dari perulangan
        """)

x = [3,4,5,2,1,10,8,77,60,50]
j = 0
maks = 0

flowchart()

# for Loop
for i in range( len(x)):
  if x[i] > maks:
    maks = x[i]
  else:
    continue

print("Nilai maks menggunakan for =", maks)
maks = 0

# while Loop
while j < len(x):
  if x[j] > maks:
    maks = x[j]
  j += 1

print("Nilai maks menggunakan while =", maks)