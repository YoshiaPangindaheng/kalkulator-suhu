import tkinter as tk
from tkinter import ttk

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
    kelvin = celcius + OFFSET_KELVIN
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

root = tk.Tk()
root.title("Kalkulator Suhu")
root.geometry("380x240")

# Ini for tema gelap neh
bg_color = "#1e1e1e"
fg_color = "#ffffff"
entry_bg = "#2a2a2a"
button_bg = "#3b3b3b"
button_hover = "#505050"
combo_bg = "#2a2a2a"

root.configure(bg=bg_color)

style = ttk.Style()
style.theme_use("clam")

style.configure("TCombobox",
                fieldbackground=combo_bg,
                background=combo_bg,
                foreground=fg_color,
                bordercolor="#555555",
                arrowcolor=fg_color)

style.map("TCombobox",
          fieldbackground=[("readonly", combo_bg)],
          foreground=[("readonly", fg_color)],
          background=[("readonly", combo_bg)])

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