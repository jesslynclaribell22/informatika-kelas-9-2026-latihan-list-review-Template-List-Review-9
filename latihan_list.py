# NAMA  : Jesslyn Claribell Salim
# KELAS : 9A
# ---------------------------------------------------------
# LATIHAN: REVIEW LIST PYTHON
#Diberikan sebuah data acak nilai ujian siswa. Buatlah program yang mengurutkan data tersebut 
#dari nilai tertinggi ke terendah. Kemudian, pisahkan 3 nilai tertinggi sebagai penerima beasiswa, 
#dan hapus nilai terendah (nilai di bawah 60) karena dianggap tidak lulus. 
#Gunakan data awal berikut: nilai_ujian = [75, 55, 90, 85, 45, 95, 80] 
# ---------------------------------------------------------

# OUTPUT
#Data nilai asli: [75, 55, 90, 85, 45, 95, 80] 
#Data setelah diurutkan (Descending): [95, 90, 85, 80, 75, 55, 45] 
#Tiga nilai tertinggi (Penerima Beasiswa): [95, 90, 85] 
#Daftar nilai yang lulus: [95, 90, 85, 80, 75]
# ---------------------------------------------------------

# Tulis kodemu di bawah ini:
print("== praktek Jesslyn Claribell ==")
nilai_ujian = [75, 55, 90, 85, 45, 95, 80]

nilai_ujian.sort(reverse=True)
print("Data nilai tertinggi ke terendah:", nilai_ujian)
top3 = nilai_ujian[:3]
print("penerima beaiswa :", top3)
nilai_lulus =[]

for nilai in nilai_ujian :
  if nilai >= 60:
    nilai_lulus.append(nilai)
print("nilai yang lulus:", nilai_lulus)


  
