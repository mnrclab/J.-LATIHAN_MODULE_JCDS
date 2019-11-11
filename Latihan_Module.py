#SOAL PERTAMA

nilai = int(input('Masukkan nilai Anda:'))

if(nilai>95) :
    print('Alhamdulillah')
elif(nilai >= 70 and nilai <=100):
    print('Lulus')
else:
    print('Hindari ya')


#SOAL KEDUA

jomblo = True

if(jomblo):
    print('Masih available')
else:
    print('Sold out')



jomblo = bool(input('Kamu masih jomblo, True/False?'))

if(Jomblo = True):
    print('Masih available')
else:
    print('Sold out')

# SOAL KETIGA

angka = int(input('Masukkan angka: '))
genap = angka % 2

if(genap == 0):
    print(f'Angka {angka} terbilang bilangan GENAP')
else:
    print(f'Angka {angka} terbilang bilangan GANJIL')



# SOAL KEEMPAT 
massa = float(input('Berapa berat badan Anda (kg): '))
tinggi1 = float(input('Berapa tinggi badan Anda (cm): '))
tinggi2 = tinggi1 / 100

IMT = round((massa / tinggi2 **2), 2)

if(IMT < 18.5):
    print(f'IMT sebesar {IMT} artinya berat badan Anda kurang')
elif(18.5 <= IMT <= 24.9):
    print(f'IMT sebesar {IMT} artinya berat badan Anda ideal')
elif(25.0 <=IMT <= 29.9):
    print(f'IMT sebesar {IMT} artinya berat badan Anda berlebih')
elif(30 <= IMT <= 39.9):
    print(f'IMT sebesar {IMT} artinya berat badan Anda sangat berlebih')
else:
    print(f'IMT sebesar {IMT} artinya Anda tergolong obesitas')


# LOOP

angka = 1

while (angka <= 10):
    print(angka)
    angka += 2


listItem = list(range(1,11,2))
print(listItem)

for item in range(1,11,2):
    print(item)


# SOAL PERTAMA LOOP

y = 'Nomor urut '

for item in range(1,11,1) :
    print(y + str(item))

SOAL KEDUA LOOP
y = 'Nomor urut '

for item in range(1,20,2) :
    print(y + str(item))

# FOR LOOP DRAWING

z =''

for item in range(0,5):
    z += ' * '

print(z)


z = ''

for item in range(0,5):
    z += '* \n'

print (z)

z = ''
for item in range(5):
    for item1 in range(5):
        z += '*'
    z += '\n'

print(z)


z = ''
for item in range(5):
    for item1 in range(0, item+1):
        z += '*'
    z += '\n'

print(z)

z = ''
for x in range(0, 5):
    for y in range(0,5-x):
        z += '*'
    z += '\n'

print(z)

z = ''
for x in range(0, 5):
    for y in range(0,5-x):
        z += ' * '
    z += '\n'
for x in range(1,5):
    for y in range(0, x+1):
        z += ' * '
    z += '\n'

print(z)

a = 1
b = 20
c = 10

for i in range(a, b, 2):
    print((c * ' ') + (i * '*'))
    c -= 1

a = 0
b = 21
c = 0

for i in range(b, a,-2):
    print((c * ' ') + (i * '*'))
    c += 1

a = 1
b = 20
c = 10

for i in range(a,b,2):
    print((c * ' ') + (b * '*'))
    c -= 1