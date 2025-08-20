import requests
from datetime import datetime

import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID") # https://api.telegram.org/bot{TOKEN}/getUpdates

def kirim_pesan():
    """
    Kirim pesan ke Telegram dengan isi pesan yang sudah ditentukan.
    
    Fungsi ini akan mengirimkan pesan ke Telegram dengan menggunakan API Telegram.
    Jika sukses, maka akan mencetak "Notif dikirim!" ke console.
    Jika gagal, maka akan mencetak error ke console.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    pesan = "Rozhak Sayangkuhhh, jangan lupa absen Asah Machine Learning hari ini ya! Aku support terus dari hati terdalam! 🥰💕"
    payload = {"chat_id": CHAT_ID, "text": pesan}
    try:
        res = requests.post(url, data=payload)
        print(f"[{datetime.now()}] Notif dikirim!")
    except Exception as e:
        print(f"Error kirim pesan: {e}")

if __name__ == "__main__":
    kirim_pesan()