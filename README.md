# 🎯 Math Guru AI

Asisten pembelajaran matematika pintar yang ditenagai oleh Google Gemini AI. Dirancang untuk membantu siswa memahami konsep matematika dengan cara yang interaktif dan menyenangkan.

## ✨ Fitur Utama
- 🤖 Berbasis Google Gemini AI (upgrade dari Ollama + Qwen)
- 🎓 Penjelasan step-by-step yang mudah dipahami
- 📝 Contoh soal yang relevan
- 💡 Pendekatan pembelajaran yang adaptif
- 🌐 Dukungan Bahasa Indonesia
- ⚡ Respons cepat dan akurat
- 🔄 Fitur retry otomatis untuk koneksi yang stabil
- 🧹 Fitur clear screen untuk antarmuka yang bersih

## 🚀 Perbandingan dengan Versi Sebelumnya

Sebelumnya:
- Menggunakan Ollama + Qwen
- Memerlukan server lokal
- Setup yang lebih kompleks

Sekarang:
- Menggunakan Google Gemini
- Cloud-based, tanpa perlu server lokal
- Setup lebih sederhana
- Performa lebih stabil

## 🛠️ Cara Menggunakan

### Prasyarat
```bash
pip install google-generativeai
pip install langchain-core
pip install tenacity


### Konfigurasi
1. Dapatkan API key dari [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Ganti `YOUR_API_KEY` dengan API key Anda di file `math_guru.py`:
```python
GOOGLE_API_KEY = "YOUR_API_KEY"


### Menjalankan Aplikasi
1. Download atau clone repository ini
```bash
git clone https://github.com/username/math-guru-ai.git
cd math-guru-ai


2. Jalankan aplikasi
```bash
python3 math_guru.py


## 📖 Penggunaan

Setelah aplikasi berjalan:
1. Ketik pertanyaan matematika Anda dalam Bahasa Indonesia
2. Tunggu respons dari AI
3. Gunakan perintah khusus:
   - Ketik `clear` untuk membersihkan layar
   - Ketik `keluar` untuk mengakhiri sesi

## 🤝 Kontribusi

Kontribusi selalu diterima! Cara berkontribusi:
1. Fork repository ini
2. Buat branch baru (`git checkout -b fitur-baru`)
3. Commit perubahan Anda (`git commit -m 'Menambahkan fitur baru'`)
4. Push ke branch tersebut (`git push origin fitur-baru`)
5. Buat Pull Request

## 📝 Lisensi

Proyek ini dilisensikan di bawah MIT License - lihat file [LICENSE](LICENSE) untuk detail.

## 🙏 Kredit

- [Google Generative AI](https://ai.google.dev/)
- [LangChain](https://www.langchain.com/)
- [Tenacity](https://tenacity.readthedocs.io/)

## 📞 Dukungan

Jika Anda menemukan masalah atau memiliki pertanyaan:
1. Buat issue di repository ini
2. Hubungi kami melalui email di: kontak@classy.id
```
