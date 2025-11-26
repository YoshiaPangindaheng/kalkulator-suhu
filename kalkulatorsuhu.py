import customtkinter as ctk
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Kalkulator Suhu")
app.geometry("420x420")
app.resizable(False, False)

def celcius_fahrenheit(celcius):
    """
    Mengkalkulasikan hasil konversi suhu dari Celcius ke Fahrenheit

    :param celcius: Nilai celcius yang akan dikonversikan
    :return: Mengembalikan hasil konversi Celcius ke Fahrenheit
    """
    OFFSET_FAHRENHEIT = 32
    RASIO_CELCIUS_FAHRENHEIT = 9/5
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
    celcius = (fahrenheit - OFFSET_FAHRENHEIT) * RASIO_CELCIUS_FAHRENHEIT
    return celcius

def fahrenheit_kelvin(fahrenheit):
    """
    Mengkalkulasikan hasil konversi suhu dari Fahrenheit ke Kelvin

    :param fahrenheit: Nilai fahrenheit yang akan dikonversikan
    :return: Mengembalikan hasil konversi Fahrenheit ke Kelvin
    """
    OFFSET_FAHRENHEIT = 32
    OFFSET_KELVIN = 273.15
    RASIO_CElCIUS_FAHRENHEIT = 5/9
    kelvin = (fahrenheit - OFFSET_FAHRENHEIT) * RASIO_CElCIUS_FAHRENHEIT + OFFSET_KELVIN
    return kelvin

def kelvin_celcius(kelvin):
    """
    Mengkalkulasikan hasil konversi suhu dari Kelvin ke Celcius

    :param kelvin: Nilai kelvin yang akan dikonversikan
    :return: Mengembalikan hasil konversi Kelvin ke Celcius
    """
    OFFSET_KELVIN = 273.15
    celcius = kelvin - OFFSET_KELVIN
    return celcius

def kelvin_fahrenheit(kelvin):
    """
    Mengkalkulasikan hasil konversi suhu dari Kelvin ke Fahrenheit

    :param kelvin: Nilai Kelvin yang akan dikonversikan
    :return: Mengembalikan hasil konversi Kelvin ke Fahrenheit
    """
    OFFSET_FAHRENHEIT = 32
    OFFSET_KELVIN = 273.15
    RASIO_CELCIUS_FAHRENHEIT = 9/5
    fahrenheit = (kelvin - OFFSET_KELVIN) * RASIO_CELCIUS_FAHRENHEIT + OFFSET_FAHRENHEIT
    return fahrenheit

frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=20, pady=20, fill="both", expand=True)

title_label = ctk.CTkLabel(
    frame, 
    text="Kalkulator Suhu",
    font=("Segoe UI", 20, "bold")
)
title_label.pack(pady=(15, 10))

input_label = ctk.CTkLabel(frame, text="Masukkan nilai suhu:", font=("Segoe UI", 13))
input_label.pack(pady=(5, 5))

entry_value = ctk.CTkEntry(frame, width=200, height=40, font=("Segoe UI", 14))
entry_value.pack()

opsi = [
    "Celsius → Fahrenheit",
    "Celsius → Kelvin",
    "Fahrenheit → Celsius",
    "Fahrenheit → Kelvin",
    "Kelvin → Celsius",
    "Kelvin → Fahrenheit"
]

dropdown_label = ctk.CTkLabel(frame, text="Pilih jenis konversi:", font=("Segoe UI", 13))
dropdown_label.pack(pady=(20, 5))

dropdown = ctk.CTkOptionMenu(frame, values=opsi, width=200, height=40, font=("Segoe UI", 14))
dropdown.pack()

# Label hasil
result_label = ctk.CTkLabel(frame, text="Hasil: -", font=("Segoe UI", 16))
result_label.pack(pady=(20, 10))

# Fungsi tombol
def konversi_suhu():
    try:
        nilai = float(entry_value.get())
        pilihan = dropdown.get()

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

        result_label.configure(text=f"Hasil: {hasil}")
    except:
        result_label.configure(text="Error: input tidak valid!")

convert_btn = ctk.CTkButton(
    frame,
    text="Konversi",
    width=200,
    height=50,
    font=("Segoe UI", 15, "bold"),
    command=konversi_suhu
)
convert_btn.pack(pady=10)

# Toggle untuk yaaa light and dark mode
def toggle_theme():
    current = ctk.get_appearance_mode()
    if current == "Dark":
        ctk.set_appearance_mode("light")
        theme_label.configure(text="Tema: Light")
    else:
        ctk.set_appearance_mode("dark")
        theme_label.configure(text="Tema: Dark")

theme_btn = ctk.CTkButton(
    frame, text="Toggle Tema",
    width=150, height=35,
    font=("Segoe UI", 12),
    command=toggle_theme
)
theme_btn.pack(pady=5)

theme_label = ctk.CTkLabel(frame, text="Tema: Dark", font=("Segoe UI", 12))
theme_label.pack()

app.mainloop()