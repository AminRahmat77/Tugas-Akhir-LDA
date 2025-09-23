from google_play_scraper import app, reviews_all
import pandas as pd

# Mendapatkan informasi dasar aplikasi
app_info = app('com.shopee.id')  # Contoh aplikasi WhatsApp

# Menampilkan informasi aplikasi
print(f"Nama Aplikasi: {app_info['title']}")
print(f"Pengembang: {app_info['developer']}")
print(f"Rating: {app_info['score']}")
print(f"Total Unduhan: {app_info['installs']}")

# Mendapatkan semua ulasan aplikasi
all_reviews = reviews_all(
    'com.shopee.id',  # ID aplikasi di Google Play Store
    sleep_milliseconds=0,  # Waktu tidur antara permintaan (bisa diatur jika diperlukan)
    lang='id',  # Bahasa ulasan (misalnya 'id' untuk Bahasa Indonesia)
    country='id'  # Negara pengguna
)

# Menampilkan beberapa ulasan pertama
for review in all_reviews[:3]:
    print(f"User: {review['userName']}")
    print(f"Rating: {review['score']}")
    print(f"Ulasan: {review['content']}\n")

# Mengonversi ulasan ke DataFrame untuk analisis lebih lanjut
df_reviews = pd.DataFrame(all_reviews)

# Menyimpan data ulasan ke file CSV
df_reviews.to_csv('google_play_reviews.csv', index=False)
print("Data ulasan telah disimpan dalam file CSV.")

