import google.generativeai as genai
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import time
import os
from typing import List
from tenacity import retry, stop_after_attempt, wait_exponential

# Konfigurasi Gemini
GENERATION_CONFIG = genai.GenerationConfig(
    temperature=0.7,
    top_p=0.95,
    max_output_tokens=2048,
)

# Masukkan API key Anda
GOOGLE_API_KEY = "<apikey-Gemini>"
genai.configure(api_key=GOOGLE_API_KEY)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_typing(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def get_system_prompt() -> str:
    return """Kamu adalah asisten guru matematika yang sabar dan membantu.
Panduan mengajar:
1. Jelaskan konsep dengan sederhana dan mudah dipahami
2. Berikan langkah penyelesaian step by step
3. Sertakan contoh yang relevan
4. Jika siswa bingung, coba pendekatan penjelasan yang berbeda
5. Dorong siswa untuk berpikir kritis
Berikan jawaban dalam bahasa Indonesia yang jelas, singkat dan edukatif dengan contoh soal jika diperlukan."""

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10),
    reraise=True
)
def send_message_with_retry(chat, message):
    return chat.send_message(message)

def create_math_tutor():
    try:
        model = genai.GenerativeModel('gemini-pro', generation_config=GENERATION_CONFIG)
        return model
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    clear_screen()
    print("\n" + "="*50)
    print_with_typing("📚 Selamat datang di Asisten Belajar Matematika!")
    print_with_typing("🎓 Saya siap membantu kamu belajar matematika")
    print_with_typing("💡 Ketik 'keluar' untuk mengakhiri sesi belajar")
    print_with_typing("📝 Ketik 'clear' untuk membersihkan layar")
    print("="*50 + "\n")

    model = create_math_tutor()
    if not model:
        print_with_typing("❌ Gagal menginisialisasi asisten. Coba lagi nanti.")
        return

    chat = model.start_chat(history=[])
    try:
        chat.send_message(get_system_prompt())
    except Exception as e:
        print(f"❌ Error saat inisialisasi: {e}")
        print("Mencoba melanjutkan...")

    while True:
        try:
            user_input = input("\n👨‍🎓 Siswa: ")
            
            if user_input.lower() == 'keluar':
                print_with_typing("\n👨‍🏫 Guru: Semangat belajar! Sampai jumpa lagi! 👋")
                break
            elif user_input.lower() == 'clear':
                clear_screen()
                chat = model.start_chat(history=[])
                try:
                    chat.send_message(get_system_prompt())
                except Exception:
                    pass
                continue
            elif not user_input.strip():
                continue

            print("\n👨‍🏫 Guru: ", end='', flush=True)
            
            try:
                response = send_message_with_retry(chat, user_input)
                print_with_typing(response.text, delay=0.02)
            except Exception as e:
                print(f"\n❌ Terjadi error dalam komunikasi: {e}")
                print("Silakan coba lagi atau tunggu beberapa saat.")
                
        except KeyboardInterrupt:
            print_with_typing("\n\n👨‍🏫 Guru: Sesi belajar diinterupsi. Sampai jumpa! 👋")
            break
        except Exception as e:
            print(f"\n❌ Terjadi error: {e}")
            print("Silakan coba lagi.")

if __name__ == "__main__":
    main()
