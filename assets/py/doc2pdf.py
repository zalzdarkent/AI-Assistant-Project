import tkinter as tk
from tkinter import filedialog
from docx2pdf import convert
import os
from tkinter import ttk

def get_filename_without_extension(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]

def is_valid_docx_file(filepath):
    return os.path.isfile(filepath) and filepath.lower().endswith(".docx")

def convert_docx_to_pdf(input_file, output_file):
    try:
        convert(input_file, output_file)
        print("Konversi berhasil. File PDF telah dibuat dan disimpan.")
        status_label.config(text="Konversi berhasil. File PDF telah dibuat dan disimpan.", foreground="green")
    except Exception as e:
        status_label.config(text=f"Terjadi kesalahan saat melakukan konversi: {str(e)}", foreground="red")

def browse_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    input_entry.delete(0, tk.END)
    input_entry.insert(0, file_path)

def perform_conversion():
    input_file = input_entry.get()

    if not is_valid_docx_file(input_file):
        status_label.config(text="Mohon pilih file Word (.docx) yang valid.", foreground="red")
        return

    output_directory = os.path.join("assets", "pdf")
    os.makedirs(output_directory, exist_ok=True)

    # Dapatkan nama file tanpa ekstensi
    filename_without_extension = get_filename_without_extension(input_file)

    # Gabungkan nama file dengan ekstensi .pdf untuk output file
    output_file = os.path.join(output_directory, f"{filename_without_extension}.pdf")

    convert_docx_to_pdf(input_file, output_file)

# Membuat GUI
root = tk.Tk()
root.title("Konversi Word ke PDF")

# Menggunakan tema "clam" dari ttk
style = ttk.Style()
style.theme_use("clam")

frame = ttk.Frame(root, padding="20")
frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

input_label = ttk.Label(frame, text="File Word (.docx):")
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
judul_label = ttk.Label(root, text="Konversi Word ke PDF", font=("Helvetica", 16, "bold"))
judul_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Informasi pembuat dan copyright di bagian bawah
footer_label = ttk.Label(root, text="Dibuat oleh Zalzdarkent", font=("Helvetica", 10))
footer_label.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

# Copyright
copyright_label = ttk.Label(root, text="© 2023 Zalzdarkent. Hak Cipta Dilindungi.", font=("Helvetica", 8))
copyright_label.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

root.mainloop()
