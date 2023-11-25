import tkinter as tk
from tkinter import messagebox
import sqlite3

# Membuat fungsi dengan nama submit_data
def submit_data():
    # Membuat space atau wadah untuk memasukkan nilai
    nama_siswa = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())
    kimia = int(entry_kimia.get())
    matematika = int(entry_matematika.get())
    pkn = int(entry_pkn.get())
    sejarah = int(entry_sejarah.get())
    ekonomi = int(entry_ekonomi.get())
    bhs_Indonesia = int(entry_bhs_Indonesia.get())
    geografi = int(entry_geografi.get())

    # Menghitung nilai untuk memprediksikan fakultas
    if biologi > fisika and biologi > inggris:
        prediksi_fakultas = 'Kedokteran'
    elif fisika > biologi and matematika > inggris:
        prediksi_fakultas = 'Teknik'
    elif ekonomi > bhs_Indonesia and ekonomi > fisika :
        prediksi_fakultas = 'Ekonomi'
    elif sejarah > biologi and sejarah > matematika :
        prediksi_fakultas = 'Fisipol'
    else:
        prediksi_fakultas = 'Bahasa'

    # Mengkoneksikan SQLite dengan codingan.
    conn = sqlite3.connect('nilai_siswa.db')
    cursor = conn.cursor()
    # Membuat tabel dengan nama nilai_siswa jika belum dibuat dalam DB Browser SQLite
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            kimia INTEGER,
            matematika INTEGER,
            pkn INTEGER,
            sejarah INTEGER,
            ekonomi INTEGER,
            bhs_Indonesia INTEGER,
            geografi INTEGER,
            prediksi_fakultas TEXT
        )
    ''')
    #Memasukkan nilai ke dalam database SQLite
    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, kimia, matematika, pkn, sejarah, ekonomi, bhs_Indonesia, geografi, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nama_siswa, biologi, fisika, inggris, kimia, matematika, pkn, sejarah, ekonomi, bhs_Indonesia, geografi, prediksi_fakultas))
    conn.commit()
    conn.close()

    messagebox.showinfo('Info', 'Data submitted successfully!')

# Membuat main window
root = tk.Tk()
root.title('Student Data Entry')

# Membuat labels dan entry widgets
label_nama = tk.Label(root, text='Nama Siswa:')
label_nama.grid(row=0, column=0, padx=10, pady=10)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1, padx=10, pady=10)

label_biologi = tk.Label(root, text='Biologi:')
label_biologi.grid(row=1, column=0, padx=10, pady=10)
entry_biologi = tk.Entry(root)
entry_biologi.grid(row=1, column=1, padx=10, pady=10)

label_fisika = tk.Label(root, text='Fisika:')
label_fisika.grid(row=2, column=0, padx=10, pady=10)
entry_fisika = tk.Entry(root)
entry_fisika.grid(row=2, column=1, padx=10, pady=10)

label_inggris = tk.Label(root, text='Inggris:')
label_inggris.grid(row=3, column=0, padx=10, pady=10)
entry_inggris = tk.Entry(root)
entry_inggris.grid(row=3, column=1, padx=10, pady=10)

label_kimia = tk.Label(root, text='kimia:')
label_kimia.grid(row=4, column=0, padx=10, pady=10)
entry_kimia = tk.Entry(root)
entry_kimia.grid(row=4, column=1, padx=10, pady=10)

label_matematika = tk.Label(root, text='matematika:')
label_matematika.grid(row=5, column=0, padx=10, pady=10)
entry_matematika = tk.Entry(root)
entry_matematika.grid(row=5, column=1, padx=10, pady=10)

label_pkn = tk.Label(root, text='pkn:')
label_pkn.grid(row=6, column=0, padx=10, pady=10)
entry_pkn = tk.Entry(root)
entry_pkn.grid(row=6, column=1, padx=10, pady=10)

label_sejarah = tk.Label(root, text='sejarah:')
label_sejarah.grid(row=7, column=0, padx=10, pady=10)
entry_sejarah = tk.Entry(root)
entry_sejarah.grid(row=7, column=1, padx=10, pady=10)

label_ekonomi = tk.Label(root, text='ekonomi:')
label_ekonomi.grid(row=8, column=0, padx=10, pady=10)
entry_ekonomi = tk.Entry(root)
entry_ekonomi.grid(row=8, column=1, padx=10, pady=10)

label_bhs_Indonesia = tk.Label(root, text='bhs_Indonesia:')
label_bhs_Indonesia.grid(row=9, column=0, padx=10, pady=10)
entry_bhs_Indonesia = tk.Entry(root)
entry_bhs_Indonesia.grid(row=9, column=1, padx=10, pady=10)

label_geografi = tk.Label(root, text='geografi:')
label_geografi.grid(row=10, column=0, padx=10, pady=10)
entry_geografi = tk.Entry(root)
entry_geografi.grid(row=10, column=1, padx=10, pady=10)

# Membuat tombol submit
submit_button = tk.Button(root, text='Submit', command=submit_data)
submit_button.grid(row=11, column=0, columnspan=2, pady=10)

# Run  Tkinter main loop
root.mainloop()