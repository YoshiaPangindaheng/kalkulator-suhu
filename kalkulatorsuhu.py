# Program Perhitungan Suhu
OFFSETFAHRENHEIT = 32
RASIOFAHRENHEIT = 1.8

celcius = int(input("Masukkan suhu (dalam bentuk celcius) disini... "))
hasil_fahrenheit = (RASIOFAHRENHEIT * celcius) + OFFSETFAHRENHEIT
print("Suhu dalam Fahrenheit adalah:", hasil_fahrenheit)

#Celcius To Kelvin
OFFSETKELVIN = 273.15
hasil_kelvin = celcius + OFFSETKELVIN
print("Suhu dalam Kelvin adalah:", hasil_kelvin)