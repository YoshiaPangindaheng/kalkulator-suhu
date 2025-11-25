import tkinter as tk
from tkinter import ttk

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

root = tk.Tk()
root.title("Kalkulator Suhu")
root.geometry("380x240")

# Label input
label_input = tk.Label(root, text="Masukkan nilai suhu:")
label_input.pack(pady=5)

entry_nilai = tk.Entry(root, width=20)
entry_nilai.pack()

# Pilihan konversi
label_pilihan = tk.Label(root, text="Pilih jenis konversi:")
label_pilihan.pack(pady=5)

opsi = [
    "Celsius → Fahrenheit",
    "Celsius → Kelvin",
    "Fahrenheit → Celsius",
    "Fahrenheit → Kelvin",
    "Kelvin → Celsius",
    "Kelvin → Fahrenheit"
]

selected_option = tk.StringVar()
selected_option.set(opsi[0])

dropdown = ttk.Combobox(root, textvariable=selected_option, values=opsi, state="readonly")
dropdown.pack()

# Label hasil
label_hasil = tk.Label(root, text="Hasil: -", font=("Arial", 12))
label_hasil.pack(pady=10)

# Fungsi tombol
def konversi_suhu():
    try:
        nilai = float(entry_nilai.get())
        pilihan = selected_option.get()

        if pilihan == "Celsius → Fahrenheit":
            hasil = celcius_fahrenheit(nilai)
        elif pilihan == "Celsius → Kelvin":
            hasil = celcius_kelvin(nilai)
        elif pilihan == "Fahrenheit → Celsius":
            hasil = fahrenheit_celcius(nilai)
        elif pilihan == "Fahrenheit → Kelvin":
            hasil = fahrenheit_kelvin(nilai)
        elif pilihan == "Kelvin → Celsius":
            hasil = kelvin_celcius(nilai)
        elif pilihan == "Kelvin → Fahrenheit":
            hasil = kelvin_fahrenheit(nilai)
        else:
            hasil = "Error"

        label_hasil.config(text=f"Hasil: {hasil}")

    except ValueError:
        label_hasil.config(text="Error: Input tidak valid!")

# Tombol konversi
btn = tk.Button(root, text="Konversi", command=konversi_suhu)
btn.pack(pady=10)

root.mainloop()