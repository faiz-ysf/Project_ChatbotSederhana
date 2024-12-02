import tkinter as tk
from tkinter import ttk, messagebox

def tambah_data():
    """
    Fungsi untuk menambahkan data ke tabel.
    Implementasikan logika pengambilan data dari input di sini.
    """
    name_choice = data_name.get()
    age_choice = data_age.get()
    breed_choice = data_breed.get()
    color_choice = data_color.get()

    if name_choice == "" or age_choice == "" or breed_choice == "" or color_choice == "":
        messagebox.showwarning("", "Please fill all fields.")
    
    tabel_data.insert("", 'end', text="", values=(name_choice, age_choice, breed_choice, color_choice))
    clear_input()
    


def clear_input():
    """
    Fungsi untuk mengosongkan semua input field setelah data ditambahkan.
    """
    data_name.delete(0, tk.END)
    data_age.delete(0, tk.END)
    data_breed.delete(0, tk.END)
    data_color.delete(0, tk.END)
    


# GUI Utama
root = tk.Tk()
root.title("Sistem Inventaris")

'''Frame untuk menyusun pengetikan data'''
data_frame = tk.Frame(root)
data_frame.pack(pady=10)

# Label Nama
label_name = tk.Label(data_frame, text="Name:")
label_name.pack(pady=5)
data_name = tk.Entry(data_frame, width=30)
data_name.pack(padx=5)

# Label Umur
label_age = tk.Label(data_frame, text="Age:")
label_age.pack(pady=5)
data_age = tk.Entry(data_frame, width=30)
data_age.pack(padx=5)

# Label Ras
label_breed = tk.Label(data_frame, text="Breed:")
label_breed.pack(pady=5)
data_breed = tk.Entry(data_frame, width=30)
data_breed.pack(padx=5)

# Label Warna
label_color = tk.Label(data_frame, text="Color:")
label_color.pack(pady=5)
data_color = tk.Entry(data_frame, width=30)
data_color.pack(padx=5)

# Tombol menambahkan data baru
add_kucing = tk.Button(data_frame, text="Add Cat", width="10", command=tambah_data)
add_kucing.pack()
kolom = ("Name", "Age", "Breed", "Color")  # Ganti sesuai soal

# Membuat Tabel beserta column dan heading
tabel_data = ttk.Treeview(root, columns=kolom, show="headings")
tabel_data.heading("Name", text="Name")
tabel_data.column("Name", width=100)
tabel_data.heading("Age", text="Age")
tabel_data.column("Age", width=100)
tabel_data.heading("Breed", text="Breed")
tabel_data.column("Breed", width=100)
tabel_data.heading("Color", text="Color")
tabel_data.column("Color", width=100)

tabel_data.pack()

# Memulai program
root.mainloop()