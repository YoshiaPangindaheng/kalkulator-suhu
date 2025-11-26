def celcius_fahrenheit(celcius):
    """
    Mengkalkulasikan hasil konversi suhu dari Celcius ke Fahrenheit

    :param celcius: Nilai celcius yang akan dikonversikan
    :return: Mengembalikan hasil konversi Celcius ke Fahrenheit
    """
    OFFSET_FAHRENHEIT = 32
    RASIO_CELCIUS_FAHRENHEIT = 5/9
    fahrenheit = (RASIO_CELCIUS_FAHRENHEIT * celcius) + OFFSET_FAHRENHEIT
    return fahrenheit

def celcius_kelvin(celcius):
    """
    Mengkalkulasikan hasil konversi suhu dari Celcius ke Fahrenheit

    :param celcius: Nilai celcius yang akan dikonversikan
    :return: Mengembalikan hasil konversi Celcius ke Fahrenheit
    """
    OFFSET_KELVIN = 273.15
    kelvin = celcius + OFFSETKELVIN
    return kelvin

def fahrenheit_celcius(fahrenheit):
    """
    Mengkalkulasikan hasil konversi suhu dari Fahrenheit ke Celcius

    :param fahrenheit: Nilai fahrenheit yang akan dikonversikan
    :return: Mengembalikan hasil konversi Fahrenheit ke Celcius
    """
    OFFSET_FAHRENHEIT = 32
    RASIO_CELCIUS_FAHRENHEIT = 5/9
    celcius = (fahrenheit - OFFSET_FAHRENHEIT) / RASIO_CELCIUS_FAHRENHEIT
    return celcius

def fahrenheit_kelvin(fahrenheit):
    """
    Mengkalkulasikan hasil konversi suhu dari Fahrenheit ke Kelvin

    :param fahrenheit: Nilai fahrenheit yang akan dikonversikan
    :return: Mengembalikan hasil konversi Fahrenheit ke Kelvin
    """
    OFFSET_FAHRENHEIT = 32
    OFFSET_KELVIN = 277.15
    RASIO_CElCIUS_FAHRENHEIT = 5/9
    kelvin = (fahrenheit - OFFSET_FAHRENHEIT) * RASIO_CElCIUS_FAHRENHEIT + OFFSET_KELVIN
    return kelvin

def kelvin_celcius(kelvin):
    """
    Mengkalkulasikan hasil konversi suhu dari Kelvin ke Celcius

    :param kelvin: Nilai kelvin yang akan dikonversikan
    :return: Mengembalikan hasil konversi Kelvin ke Celcius
    """
    OFFSET_KELVIN = 277.15
    celcius = kelvin - OFFSET_KELVIN
    return celcius
def kelvin_fahrenheit(kelvin):
    """
    Mengkalkulasikan hasil konversi suhu dari Kelvin ke Fahrenheit

    :param kelvin: Nilai Kelvin yang akan dikonversikan
    :return: Mengembalikan hasil konversi Kelvin ke Fahrenheit
    """
    OFFSET_FAHRENHEIT = 32
    OFFSET_KELVIN = 277.15
    RASIO_CELCIUS_FAHRENHEIT = 5/9
    fahrenheit = (kelvin - OFFSET_KELVIN) * RASIO_CELCIUS_FAHRENHEIT + OFFSET_FAHRENHEIT
    return fahrenheit

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
        print(celcius_kelvin(celcius))
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
