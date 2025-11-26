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

# Tema for kedua mode light dan dark
themes = {
    "light": {
        "bg": "#ffffff",
        "fg": "#000000",
        "entry_bg": "#f0f0f0",
        "button_bg": "#e0e0e0",
        "button_hover": "#c8c8c8",
        "combo_bg": "#f0f0f0",
        "combo_fg": "#000000"
    },
    "dark": {
        "bg": "#1e1e1e",
        "fg": "#ffffff",
        "entry_bg": "#2a2a2a",
        "button_bg": "#3b3b3b",
        "button_hover": "#505050",
        "combo_bg": "#2a2a2a",
        "combo_fg": "#ffffff"
    }
}

current_theme = "dark"   # default

# Fungsi untuk bisa mengaplikasikan tema setiap kali tekan tombol
def apply_theme(theme_name):
    global current_theme
    current_theme = theme_name
    t = themes[theme_name]

    # Window background
    root.configure(bg=t["bg"])

    # Label colors
    label_input.config(bg=t["bg"], fg=t["fg"])
    label_pilihan.config(bg=t["bg"], fg=t["fg"])
    label_hasil.config(bg=t["bg"], fg=t["fg"])
    theme_label.config(bg=t["bg"], fg=t["fg"])

    # Entry style
    entry_nilai.config(bg=t["entry_bg"], fg=t["fg"], insertbackground=t["fg"])

    # Button style
    btn.config(bg=t["button_bg"], fg=t["fg"], activebackground=t["button_hover"])
    toggle_btn.config(bg=t["button_bg"], fg=t["fg"], activebackground=t["button_hover"])

    # Combobox style
    style.configure(
        "TCombobox",
        fieldbackground=t["combo_bg"],
        background=t["combo_bg"],
        foreground=t["combo_fg"],
        arrowcolor=t["combo_fg"]
    )
    dropdown.configure(background=t["combo_bg"])

style = ttk.Style()
style.theme_use("clam")

label_input = tk.Label(root, text="Masukkan nilai suhu:")
label_input.pack(pady=5)

entry_nilai = tk.Entry(root, width=20, relief="solid", borderwidth=1)
entry_nilai.pack()

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
dropdown.pack(pady=2)

label_hasil = tk.Label(root, text="Hasil: -", font=("Arial", 12))
label_hasil.pack(pady=15)

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
btn = tk.Button(root, text="Konversi", command=konversi_suhu, relief="flat", padx=10, pady=5)
btn.pack(pady=5)

def toggle_theme():
    if current_theme == "dark":
        apply_theme("light")
        theme_label.config(text="Tema: Light")
    else:
        apply_theme("dark")
        theme_label.config(text="Tema: Dark")

toggle_btn = tk.Button(root, text="Toggle Theme", command=toggle_theme, relief="flat", padx=10, pady=5)
toggle_btn.pack(pady=10)

theme_label = tk.Label(root, text="Tema: Dark")
theme_label.pack()

apply_theme("dark")

root.mainloop()