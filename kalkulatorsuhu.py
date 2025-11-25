def celcius_fahrenheit(celcius):
    """
    Mengkalkulasikan hasil konversi suhu dari Celcius ke Fahrenheit

    :param celcius: Nilai celcius yang akan dikonversikan
    :return: Mengembalikan hasil konversi Celcius ke Fahrenheit
    """
    OFFSETFAHRENHEIT = 32
    RASIOFAHRENHEIT = 1.8
    fahrenheit = (RASIOFAHRENHEIT * celcius) + OFFSETFAHRENHEIT
    return fahrenheit

def celcius_kelvin(celcius):
    """
    Mengkalkulasikan hasil konversi suhu dari Celcius ke Fahrenheit

    :param celcius: Nilai celcius yang akan dikonversikan
    :return: Mengembalikan hasil konversi Celcius ke Fahrenheit
    """
    OFFSETKELVIN = 273.15
    kelvin = celcius + OFFSETKELVIN
    return kelvin

def cetak_hasil(konversi):
    """
    Memilih Jenis konversi kemudian mencetak hasil kalkulasi suhu

    :param konversi: Menentukan Jenis Konversi
    """
    if konversi == 1:
        celcius = int(input("Input Derajat Celcius: "))
        print(celcius_fahrenheit(celcius))
    elif konversi == 2:
        celcius = int(input("Input Derajat Celcius: "))
        print() # Masukkan Fungsi kalkulasi disini
    elif konversi == 3:
        fahrenheit = int(input("Input Derajat Fahrenheit: "))
        print() # Masukkan Fungsi kalkulasi disini
    elif konversi == 4:
        fahrenheit = int(input("Input Derajat Fahrenheit: "))
        print() # Masukkan Fungsi kalkulasi disini
    elif konversi == 5:
        kelvin = int(input("Input Derajat Kelvin: "))
        print() # Masukkan Fungsi kalkulasi disini
    elif konversi == 6:
        kelvin = int(input("Input Derajat Kelvin: "))
        print() # Masukkan Fungsi kalkulasi disini

# Main Program
print("Program Kalkulator Suhu")
print("Pilih Jenis Konversi:")
print(f"1 = C -> F \n"
      f"2 = C -> K \n"
      f"3 = F -> C \n"
      f"4 = F -> K \n"
      f"5 = K -> C \n"
      f"6 = K -> F"
      )

pilihan = int(input())
cetak_hasil(pilihan)