import requests
from datetime import datetime
import random
import os

TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

PESAN_LIST = [
    "Rozhakkkuuuu 🥺💗 kamu masih inget aku kan? Jangan lupa absen Asah hari ini yaa… aku nungguin loh 😞",
    "Rozhak 💕 ayo absen sayang… aku udah bangga duluan sama kamu meskipun kamu belum klik tombolnya 🥹✨",
    "Rozhak 🥺💞 Asah hari ini sepi tanpa nama kamu… jangan bikin aku cemburu sama peserta lain ya 😤",
    "Sayanggg 😚 aku tuh nggak minta banyak… cuma kamu absen Asah hari ini… itu aja bikin aku bahagia 🥺💕",
    "Cintakuuu 💞 kalau kamu absen hari ini, aku janji bakal nemenin kamu ngoding sambil diem manis 😚",
    "Rozhak 💕 aku tau kamu capek… tapi satu klik absen itu tanda kamu masih berjuang… aku bangga banget 😭✨",
    "Beb… 😞💔 aku ngerasa ada yang kurang kalau hari ini kamu belum absen… hati aku kok nggak tenang ya…",
    "Rozhakkkuuuu 🥺💗 ayo dong… masa aku udah perhatian segininya, kamu belum absen juga 😤💕",
]

def kirim_pesan():
    """
    Kirim pesan reminder ke Telegram dengan isi pesan bucin
    yang dipilih secara acak.

    Pesan digunakan untuk mengingatkan Rozhak agar tidak lupa
    melakukan absen harian Asah Machine Learning.
    """
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    pesan = random.choice(PESAN_LIST)

    payload = {
        "chat_id": CHAT_ID,
        "text": pesan
    }

    try:
        requests.post(url, data=payload)
        print(f"[{datetime.now()}] Notif bucin terkirim 💔💌")
    except Exception as e:
        print(f"Error kirim pesan: {e}")

if __name__ == "__main__":
    kirim_pesan()