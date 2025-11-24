# Program Perhitungan Suhu
OFFSETFAHRENHEIT = 32
RASIOFAHRENHEIT = 1.8

celcius = int(input("Masukkan suhu (dalam bentuk celcius) disini... "))
hasil_fahrenheit = (RASIOFAHRENHEIT * celcius) + OFFSETFAHRENHEIT
print("Suhu dalam Fahrenheit adalah:", hasil_fahrenheit)
