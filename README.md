Latent Dirichlet Allocation Menggunakan Metode Gibbs Sampling Topik Modeling pada Ulasan Produk di Aplikasi E-Commerce

📌 Deskripsi

Repository ini berisi implementasi penelitian Tugas Akhir berjudul:
"Latent Dirichlet Allocation Menggunakan Metode Gibbs Sampling untuk Topik Modeling pada Ulasan Produk di Aplikasi E-Commerce"
Penelitian dilakukan oleh Amin Rahmat (152019090), Program Studi Informatika, Institut Teknologi Nasional Bandung, 2025.

Fokus utama penelitian adalah penerapan metode Latent Dirichlet Allocation (LDA) dengan teknik Gibbs Sampling untuk menganalisis ulasan produk pada aplikasi Zalora yang diambil dari Google Play Store.

🎯 Tujuan Penelitian
-Menerapkan LDA dengan Gibbs Sampling untuk mengidentifikasi topik-topik dalam ulasan produk.
-Membandingkan hasil topik yang diperoleh menggunakan LDA dengan dan tanpa Gibbs Sampling.
-Mengukur kualitas model menggunakan Coherence Score.

📂 Dataset
Sumber data: 2000 ulasan produk aplikasi Zalora.
Data diperoleh dengan teknik crawling dari Google Play Store.
Format data: .csv dengan fitur:
username → Nama pengguna
content → Isi ulasan
score → Penilaian (rating)

⚙️ Metode

1. Preprocessing Teks
Case folding
Punctuation removal
Tokenizing
Stopwords removal

2. Pemodelan Topik
Latent Dirichlet Allocation (LDA)
Gibbs Sampling

3. Evaluasi Model
Menggunakan Coherence Score

📊 Hasil Utama
LDA dengan Gibbs Sampling menghasilkan topik tentang kualitas produk dengan coherence score = 0.6298.
LDA tanpa Gibbs Sampling menghasilkan topik tentang harga produk dengan coherence score = 0.4630.
Hasil menunjukkan Gibbs Sampling meningkatkan stabilitas dan kualitas topik yang terbentuk.

📈 Visualisasi Hasil
 Research Flow

 <img width="766" height="562" alt="Alur" src="https://github.com/user-attachments/assets/08ee3c78-9d6e-440d-b72b-5c6e258a2b5e" />

 
