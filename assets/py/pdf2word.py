import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter
import os
from tkinter import ttk

def get_filename_without_extension(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]

def is_valid_pdf_file(filepath):
    return os.path.isfile(filepath) and filepath.lower().endswith(".pdf")

def convert_pdf_to_docx(input_file, output_file):
    try:
        cv = Converter(input_file)
        cv.convert(output_file)
        cv.close()
        print("Konversi berhasil. File Word telah dibuat dan disimpan.")
        status_label.config(text="Konversi berhasil. File Word telah dibuat dan disimpan.", foreground="green")
    except Exception as e:
        status_label.config(text=f"Terjadi kesalahan saat melakukan konversi: {str(e)}", foreground="red")

def browse_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def perform_conversion():
    input_file = input_entry.get()

    if not is_valid_pdf_file(input_file):
        status_label.config(text="Mohon pilih file PDF (.pdf) yang valid.", foreground="red")
        return

    output_directory = os.path.join("assets", "word")
    os.makedirs(output_directory, exist_ok=True)

    # Dapatkan nama file tanpa ekstensi
    filename_without_extension = get_filename_without_extension(input_file)

    # Gabungkan nama file dengan ekstensi .docx untuk output file
    output_file = os.path.join(output_directory, f"{filename_without_extension}.docx")

    convert_pdf_to_docx(input_file, output_file)

# Membuat GUI
root = tk.Tk()
root.title("Konversi PDF ke Word")

# Menggunakan tema "clam" dari ttk
style = ttk.Style()
style.theme_use("clam")

frame = ttk.Frame(root, padding="20")
frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

input_label = ttk.Label(frame, text="File PDF (.pdf):")
input_label.grid(row=0, column=0, padx=5, pady=5)

input_entry = ttk.Entry(frame, width=50)
input_entry.grid(row=0, column=1, padx=5, pady=5)

browse_input_button = ttk.Button(frame, text="Pilih File", command=browse_input_file)
browse_input_button.grid(row=0, column=2, padx=5, pady=5)

convert_button = ttk.Button(frame, text="Konversi", command=perform_conversion)
convert_button.grid(row=1, column=1, padx=5, pady=10)

# Konfigurasi kolom untuk tombol konversi berada di tengah
frame.columnconfigure(1, weight=1)

status_label = ttk.Label(frame, text="", foreground="green")
status_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Judul di bagian atas
judul_label = ttk.Label(root, text="Konversi PDF ke Word", font=("Helvetica", 16, "bold"))
judul_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Informasi pembuat dan copyright di bagian bawah
footer_label = ttk.Label(root, text="Dibuat oleh [Zalzdarkent]", font=("Helvetica", 10))
footer_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

# Copyright
copyright_label = ttk.Label(root, text="© 2023 [Zalzdarkent]. Hak Cipta Dilindungi.", font=("Helvetica", 8))
copyright_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

root.mainloop()
