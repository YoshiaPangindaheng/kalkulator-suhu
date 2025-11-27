import customtkinter as ctk
import threading
import vlc
import yt_dlp

SIDEBAR_COLORS = {
    "Dark": {
        "sidebar": "#1f1f1f",
        "submenu": "#272727",
        "button": "#2f2f2f",
        "button_hover": "#3a3a3a",
        "text": "white"
    },
    "Light": {
        "sidebar": "#f2f2f2",
        "submenu": "#ffffff",
        "button": "#e6e6e6",
        "button_hover": "#d5d5d5",
        "text": "black"
    }
}

mini_player = None
is_paused = False

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Kalkulator Suhu")
app.geometry("1400x800")
app.minsize(1100, 700)

app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(3, weight=1)
app.grid_columnconfigure(2, weight=0)
app.grid_rowconfigure(0, weight=1)

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
    RASIO_FAHRENHEIT_CELCIUS = 5/9
    celcius = (fahrenheit - OFFSET_FAHRENHEIT) * RASIO_FAHRENHEIT_CELCIUS
    return celcius

def fahrenheit_kelvin(fahrenheit):
    """
    Mengkalkulasikan hasil konversi suhu dari Fahrenheit ke Kelvin

    :param fahrenheit: Nilai fahrenheit yang akan dikonversikan
    :return: Mengembalikan hasil konversi Fahrenheit ke Kelvin
    """
    OFFSET_FAHRENHEIT = 32
    OFFSET_KELVIN = 273.15
    RASIO_FAHRENHEIT_KELVIN = 5/9
    kelvin = (fahrenheit - OFFSET_FAHRENHEIT) * RASIO_FAHRENHEIT_KELVIN + OFFSET_KELVIN
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
    RASIO_FAHRENHEIT = 9/5
    fahrenheit = (kelvin - OFFSET_KELVIN) * RASIO_FAHRENHEIT + OFFSET_FAHRENHEIT
    return fahrenheit

player = None

def get_audio_url(url):
    ydl_opts = {
        "format": "bestaudio/best",
        "quiet": True,
        "noplaylist": True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        return info["url"]

def play_youtube(url, status_label):
    global player, is_paused
    status_label.configure(text="Mengambil stream...")

    try:
        audio_url = get_audio_url(url)

        if player:
            player.stop()

        player = vlc.MediaPlayer(audio_url)
        player.play()
        is_paused = False
        status_label.configure(text="Memutar musik...")
    except Exception as e:
        status_label.configure(text=f"Error: {str(e)}")

def pause_resume_audio(status_label, btn):
    global player, is_paused
    if not player:
        return

    if not is_paused:
        player.pause()
        is_paused = True
        status_label.configure(text="Paused")
        btn.configure(text="Resume")
    else:
        player.play()
        is_paused = False
        status_label.configure(text="Playing")
        btn.configure(text="Pause")

def stop_audio(status_label):
    global player, is_paused
    if player:
        player.stop()
        status_label.configure(text="Stopped")
        is_paused = False

frame = ctk.CTkFrame(app, corner_radius=15)
frame.grid(row=0, column=2, padx=40, pady=40, sticky="n")

frame.grid_columnconfigure(0, weight=1)

title_label = ctk.CTkLabel(
    frame,
    text="Konversi Suhu",
    font=("Segoe UI", 40, "bold")
)
title_label.pack(pady=(40, 20))

ctk.CTkLabel(frame, text="Masukkan nilai suhu:", font=("Segoe UI", 22)).pack(pady=10)
entry_value = ctk.CTkEntry(frame, width=350, height=50, font=("Segoe UI", 20))
entry_value.pack(pady=10)

opsi = [
    "Celsius → Fahrenheit",
    "Celsius → Kelvin",
    "Fahrenheit → Celsius",
    "Fahrenheit → Kelvin",
    "Kelvin → Celsius",
    "Kelvin → Fahrenheit"
]

ctk.CTkLabel(frame, text="Pilih jenis konversi:", font=("Segoe UI", 22)).pack(pady=15)
dropdown = ctk.CTkOptionMenu(frame, values=opsi, width=350, height=50, font=("Segoe UI", 20))
dropdown.pack(pady=10)

result_label = ctk.CTkLabel(frame, text="Hasil: -", font=("Segoe UI", 34))
result_label.pack(pady=40)

sidebar_buttons = []

def sidebar_item(parent, icon, text, command=None):
    theme = ctk.get_appearance_mode()
    colors = SIDEBAR_COLORS[theme]

    btn = ctk.CTkButton(
        parent,
        height=38,
        width=200,
        corner_radius=6,
        fg_color=colors["button"],
        hover_color=colors["button_hover"],
        text=f"{icon}  {text}",
        anchor="w",
        text_color=colors["text"],
        font=("Segoe UI", 16),
        command=command
    )
    btn.pack(fill="x", padx=10, pady=2)

    sidebar_buttons.append(btn)

    return btn

sidebar = ctk.CTkFrame(app, width=230, corner_radius=0, fg_color="#1f1f1f")
sidebar.grid(row=0, column=0, sticky="nsw")
sidebar.grid_rowconfigure(99, weight=1)  # push bottom items down

# Sidebar Header (Logo area)
logo_frame = ctk.CTkFrame(sidebar, fg_color="transparent")
logo_frame.pack(fill="x", pady=(15, 10))

ctk.CTkLabel(
    logo_frame,
    text="Kalkulator Suhu",
    anchor="w",
    font=("Segoe UI", 20, "bold")
).pack(padx=20, anchor="w")

def sidebar_item(parent, icon, text, command=None):
    theme = ctk.get_appearance_mode()
    colors = SIDEBAR_COLORS[theme]

    btn = ctk.CTkButton(
        parent,
        height=38,
        width=200,
        corner_radius=6,
        fg_color=colors["button"],
        hover_color=colors["button_hover"],
        text=f"{icon}  {text}",
        anchor="w",
        text_color=colors["text"],
        font=("Segoe UI", 16),
        command=command
    )
    btn.pack(fill="x", padx=10, pady=2)

    sidebar_buttons.append(btn)

    return btn

sidebar_item(sidebar, "◼", "Konversi Suhu", None)

# Pemisah
ctk.CTkFrame(sidebar, height=1, fg_color="#3a3a3a").pack(fill="x", pady=(8, 8))

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
    width=300,
    height=60,
    font=("Segoe UI", 20, "bold"),
    command=konversi_suhu
)
convert_btn.pack(pady=20)

# Toggle untuk yaaa light and dark mode
def toggle_theme():
    current = ctk.get_appearance_mode()
    new_theme = "light" if current == "Dark" else "dark"
    ctk.set_appearance_mode(new_theme)
    update_sidebar_theme()

sidebar_item(sidebar, "🌗", "Toggle Tema", toggle_theme)

theme_btn = ctk.CTkButton(
    frame, text="Toggle Tema",
    width=200, height=40,
    font=("Segoe UI", 16),
    command=toggle_theme
)
theme_btn.pack(pady=10)

def toggle_music():
    if music_frame.winfo_viewable():
        music_frame.pack_forget()
    else:
        music_frame.pack(fill="x", padx=10, pady=(0, 10))

music_toggle_btn = sidebar_item(sidebar, "🎵", "Musik YouTube", toggle_music)

music_frame = ctk.CTkFrame(sidebar, fg_color="#272727", corner_radius=8)
music_frame.pack(fill="x", padx=10, pady=(0, 10))

ctk.CTkLabel(music_frame, text="YouTube Audio", anchor="w", font=("Segoe UI", 14)).pack(pady=(8, 5), padx=10)

url_entry = ctk.CTkEntry(music_frame, width=180, placeholder_text="URL YouTube")
url_entry.pack(pady=5, padx=10)

status_label = ctk.CTkLabel(music_frame, text="Status: Idle", anchor="w", font=("Segoe UI", 13))
status_label.pack(pady=5, padx=10)

def start_music():
    threading.Thread(target=play_youtube, args=(url_entry.get(), status_label), daemon=True).start()

ctk.CTkButton(music_frame, text="Play", width=180, command=start_music).pack(pady=3)
pause_btn = ctk.CTkButton(music_frame, text="Pause", width=180,
                          command=lambda: pause_resume_audio(status_label, pause_btn))
pause_btn.pack(pady=3)
ctk.CTkButton(music_frame, text="Stop", width=180,
              command=lambda: stop_audio(status_label)).pack(pady=3)

# Separator
ctk.CTkFrame(sidebar, height=1, fg_color="#3a3a3a").pack(fill="x", pady=(8, 8))

def update_sidebar_theme():
    theme = ctk.get_appearance_mode()
    colors = SIDEBAR_COLORS[theme]

    # Sidebar background
    sidebar.configure(fg_color=colors["sidebar"])

    # Submenu
    music_frame.configure(fg_color=colors["submenu"])

    # Teks di depe submenu
    status_label.configure(text_color=colors["text"])
    url_entry.configure(text_color=colors["text"])

    # Tombol di depe submenu
    pause_btn.configure(
        fg_color=colors["button"],
        hover_color=colors["button_hover"],
        text_color=colors["text"]
    )

    # Update tombol di menu sidebar
    for btn in sidebar_buttons:
        btn.configure(
            fg_color=colors["button"],
            hover_color=colors["button_hover"],
            text_color=colors["text"]
        )

update_sidebar_theme()

app.mainloop()