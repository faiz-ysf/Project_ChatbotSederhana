import tkinter as tk
from tkinter import messagebox
import time
import random
import webbrowser


'''
Fungsi Sapaan Chatbot
'''
daftar_respon = {"hai": "Hai! Ada yang bisa saya bantu?", 
                "apa kabar": "Saya baik!, terima kasih! bagaimana kabarmu?", 
                "Siapa namamu?": "Namaku adalah Chatbot!!!!"
}

def sapaan_chatbot():
     jawaban_user = str(space.get().strip().lower())
     respon_bot = None

     for key in daftar_respon:
        if key in jawaban_user:  
            respon_bot = daftar_respon[key]
            break

     if not respon_bot:
        respon_bot = "Maaf, saya belum mengerti pertanyaan apa itu. Bisa coba yang lain!"

     T.insert(tk.END, f"User: {jawaban_user}\n")
     T.insert(tk.END, f"Chatbot: {respon_bot}\n")

     space.delete(0, tk.END)

'''
Fungsi-fungsi dasar
'''
daftar_lelucon = {
     'Kenapa di keyboard komputer ada tulisan ENTER? soalnya kalau tulisannya ENTAR, programnya nggak jalan-jalan.', 
     'Apakah itu, yang jauh di mata dekat di hati? Usus.', 
     'Saya tadi beli obat tidur di apotek, pas pulang saya bawa pelan-pelan takut obatnya bangun',
     'Kala cinta masih mandang fisik, suruh aja pacaran sama ikan karena ikan banyak fisiknya.',
     'Kendaraan apa yang bunyinya imut? Kereta, naik kereta api cute cute cute... ',
     'Gajah apa yang paling baik hati? Gajahat',
     'Huruf apa yang paling kedinginan? Huruf B. Karena berada di tengah-tengah AC.',
     "Bundaran HI kalau diputerin dua kali jadi apa pak? HIHI.",
     'Sayur apa yang pintar nyanyi? Kolplay.',
     'Kalau ditutup kelihatan, tapi kalau dibuka malah nggak ada. Apa hayo? Pintu rel kereta api.',
     'Gerakan apa yang paling susah dilakuin? Move on'
} 

def lelucon_lucu():
     pilih_lelucon = random.choice(list(daftar_lelucon))

     T.insert(tk.END, f"User: buat lelucon\n")
     T.insert(tk.END, f"Chatbot: {pilih_lelucon}\n")

def waktu_kini():
     waktu_sekarang = time.strftime("%H:%M:%S", 
             time.localtime())
     
     T.insert(tk.END, f"User: tanya jam\n")
     T.insert(tk.END, f"Chatbot: Saat ini pukul {waktu_sekarang}\n")

def rick_roll():
     T.insert(tk.END, f"User: xyz\n")
     webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

'''
Fungsi Matematika
'''

jawaban_benar = 0

def soal_matematika():
     global jawaban_benar
     
     a = random.randrange(1, 9)
     b = random.randrange(1, 9)

     pilihan_soal = f"{a} + {b}" 
     jawaban_benar += a + b

     T.insert(tk.END, f"User: beri aku soal matematika\n")
     T.insert(tk.END, f"Chatbot: {pilihan_soal}\n")

def jawaban_mtk():
     jawaban_user = space.get().strip()  


     T.insert(tk.END, f"User: {jawaban_user}\n")
     
     while jawaban_user == '':
          root.update()
          root.wait_variable(space)

          jawaban_user = space.get().strip()

     while not(jawaban_user.isnumeric()):
          T.insert(tk.END, "Masukkan angka yang valid sebagai jawaban. \n")
          space.delete(0, tk.END)

          root.update()
          root.wait_variable(space)

          jawaban_user = space.get().strip()

     if int(jawaban_user) == int(jawaban_benar):
          T.insert(tk.END, "Chatbot: Benar! Jawabanmu tepat. 😊 \n")
          button_space.config(command=sapaan_chatbot)
     else:
          T.insert(tk.END, f"Chatbot: Salah, jawaban yang benar adalah {jawaban_benar}\n")
          button_space.config(command=sapaan_chatbot)
     space.delete(0, tk.END)  

def klik_mtk(event=None):
     button_space.config(command=jawaban_mtk)


''' 
Fungsi opsi sub-menu
'''

def pilihan_file(opsi):
     if opsi == "hapus_sesi":
          T.delete("1.0", tk.END)
          messagebox.showinfo("Reset", "Sesi telah direset!")
          T.insert(tk.END, 'Chatbot: Halo! Ada yang bisa saya bantu?\n')
     elif opsi == "simpan_sesi":
          sesi_chatlog = T.get("1.0", tk.END)
          waktu_sekarang = time.strftime("%Y-%m-%d_%H-%M-%S", 
             time.localtime())
          penamaan_file = f"chat_session_{waktu_sekarang}.txt"
          try:
               with open(penamaan_file, "w+", encoding="utf-8") as file:
                    file.write(sesi_chatlog)
                    messagebox.showinfo("Sukses", f"Sesi percakapan berhasil disimpan sebagai {penamaan_file}")
          except Exception:
               messagebox.showinfo("Info", "Tidak ada sesi untuk disimpan")

def pilihan_tema():
     root.configure(bg="#323232")
     T.configure(bg="#000000", fg="#FFFFFF", insertbackground="#FFFFFF")

def tentang_program():
     messagebox.showinfo("Tentang Aplikasi", "Aplikasi Chatbot ini dikembangkan oleh Faiz Yusuf Ridwan dari FASILKOM UI di tahun 2024.\nSemoga aplikasi ini dapat menjadi pembelajaran yang bermanfaat, have a great day!") 

# Program title
root = tk.Tk()
root.title("Chatbot Sederhana!")
root.geometry("500x500")
root.configure(bg="white")

''' Pembuatan Sub Menu'''

# Menu dan Sub Menu
menu = tk.Menu(root)  

# Pilihan File
simpan_file = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=simpan_file)  # Gunakan 'menu', bukan 'command'
simpan_file.add_command(label='Simpan Sesi', command=lambda: pilihan_file("simpan_sesi"))
simpan_file.add_command(label='Reset Sesi', command=lambda: pilihan_file("hapus_sesi"))
simpan_file.add_separator()
simpan_file.add_command(label='Keluar', command=root.destroy)

# Pilihan Tema
pilih_tema = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Tema', menu=pilih_tema)  
pilih_tema.add_command(label='Ubah Tema', command=pilihan_tema)

# Tentang Program
mengenai_program = tk.Menu(menu, tearoff=0)
menu.add_cascade(label='Tentang', menu=mengenai_program)  
mengenai_program.add_command(label='Tentang Aplikasi', command= tentang_program)

# Menampilkan menu pada root
root.config(menu=menu)

'''The Program main text chatbot'''

# Text frame 
text_frame = tk.Frame(root)
text_frame.pack(fill="both", expand=True, padx=5, pady=5) 
# vertical scrollbar
scrollbar = tk.Scrollbar(text_frame)
scrollbar.pack(side="right", fill="y")

# Chatbot
T = tk.Text(text_frame, height=20, width=60, yscrollcommand=scrollbar.set, wrap="word")
T.pack(side="left", fill="both", expand=True)
scrollbar.config(command=T.yview)

T.insert(tk.END, 'Chatbot: Halo! Ada yang bisa saya bantu?\n')

'''The program Button Functionality'''

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)  

# "Buat Lelucon" Button
button1 = tk.Button(button_frame, text="Buat Lelucon", width=10, command=lelucon_lucu)
button1.pack(side="left", padx=5)

# "Tanya Jam" Button
button2 = tk.Button(button_frame, text="Tanya Jam", width=10, command=waktu_kini)
button2.pack(side="left", padx=5)

# "Soal Matematika" Button
button3 = tk.Button(button_frame, text="Soal Matematika", width=15, command=soal_matematika)
button3.pack(side="left", padx=5)
button3.bind("<Button-1>", klik_mtk)

# "XYZ" Button
button4 = tk.Button(button_frame, text="XYZ", width=10, command=rick_roll)
button4.pack(side="left", padx=5)

# Entering new message
space_frame = tk.Frame(root)
space_frame.pack(pady=10)

space = tk.Entry(space_frame, width=50)
space.pack(side="left", padx=5)

button_space = tk.Button(space_frame, text="Enter", width=10, command=sapaan_chatbot)
button_space.pack(side="right", padx=5)

root.mainloop()

# Memulai program
root.mainloop()
