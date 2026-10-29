print("===============================================")
print("          PROGRAM KONVERSI & GEOMETRI       ")
print("===============================================")

#Faren to cel
def ftoc(farenheit):
    celci= (farenheit-32)*5/9
    return celci

farenheit= float(input("input nilai farenheit"))
nilai_celci= ftoc(farenheit)
print("nilai konversi celcius : ", nilai_celci)
print("===========================================")

#celci to faren
def ctof(celci):
    farenheit= (celci*9/5)+ 32
    return farenheit

celci = float(input("Input nilai celcius: "))
nilai_faren = ctof(celci)
print("Nilai konversi farenheit :", nilai_faren)

print("===========================================")

#faren to reamur
def ftor (farenheit):
    reamur= (farenheit-32)*4/9
    return reamur

reamur= float(input("masukan nilai reamur: "))
nilai_reamur= ftor(farenheit) 
print("Nilai Konversi Reamur:", nilai_reamur)
print("===========================================")

#celci to reamur
def ctor(celci):
    reamur= celci*4/5
    return reamur

reamur= float(input("masukan nilai celcius: "))
nilai_reamur= ctor(celci)
print("Nilai Konversi Reamur:", nilai_reamur)
print("===========================================")

#reamur to celci
def rtoc(reamur):
    celci= reamur*5/4
    return celci

celci= float(input("masukan nilai reamur: "))
nilai_celci= rtoc(reamur)
print("Nilai Konversi Celcius: ", nilai_celci)
print("============================================")

#Hitung luas lingkaran
def luling(jari):
    pi=22/7
    luasling= pi*pow(jari,2)
    return luasling

jari=float(input("Masukan jari-jari: "))
luas_lingkaran= luling(jari)
print("Luas Lingkaran adalah: ", luas_lingkaran)
print("==================================================")

#hitung luas permukaan tabung
def luperta(jari,tinggi):
    pi= 22/7
    luas_luperta= 2*pi*jari*(jari+tinggi)
    return luas_luperta

jari= float(input("masukan nilai jari-jari: "))
tinggi=float(input("masukan nilai tinggi: "))
luas_permukaan= luperta (jari,tinggi)
print("Luas Permukaan Tabung adalah: ",luas_permukaan)
print("=================================================")

#hitung volume tabung
def voltab(jari,tinggi):
    pi= 22/7
    volumetab= pi*pow(jari,2)*tinggi
    return volumetab

jari= float(input("masukan nilai jari-jari: "))
tinggi= float(input("masukan nilai tinggi: "))
volume= voltab(jari,tinggi)
print("Volume tabung adalah: ", volume)
print("===================================================")
print("                 Program Selesai                   ")
print("===================================================")