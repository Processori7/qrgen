from amzqr import amzqr
import os
import tkinter as tk
from tkinter import ttk, filedialog

def generate_qr_code():
    try:
        words = qr_text_entry.get()
        if words == "":
            raise Exception("Введите текст или ссылку")
        path = qr_image_path_entry.get()
        colorized = colorized_checkbox.get()
        save_name = qr_save_name_entry.get()
        version = int(version_combobox.get())
        contrast = float(contrast_entry.get())
        brightness = float(brightness_entry.get())
        extension = ext_combobox.get()
        version, level, qr_name = amzqr.run(
            words,
            version=version,
            level='H',
            picture=path,
            colorized=colorized,
            contrast=contrast,
            brightness=brightness,
            save_name=save_name + extension,
            save_dir=os.getcwd()
        )

        result_label.config(text=f"QR code generated: {qr_name}")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

def browse_image():
    file_path = filedialog.askopenfile()
    qr_image_path_entry.delete(0, tk.END)
    qr_image_path_entry.insert(0, file_path.name)

root = tk.Tk()
root.title("QR Code Generator")

qr_text_label = tk.Label(root, text="Введите текст или ссылку:")
qr_text_label.grid(row=0, column=0, padx=10, pady=10)

qr_text_entry = tk.Entry(root)
qr_text_entry.grid(row=0, column=1, padx=10, pady=10)

qr_image_path_label = tk.Label(root, text="Выберите изображение:")
qr_image_path_label.grid(row=1, column=0, padx=10, pady=10)

qr_image_path_entry = tk.Entry(root)
qr_image_path_entry.grid(row=1, column=1, padx=10, pady=10)

browse_button = tk.Button(root, text="Файлы", command=browse_image)
browse_button.grid(row=1, column=2, padx=10, pady=10)

colorized_checkbox = tk.BooleanVar()
colorized_checkbox_button = tk.Checkbutton(root, text="Цветной QR код", variable=colorized_checkbox)
colorized_checkbox_button.grid(row=2, column=0, padx=10, pady=10)

qr_save_name_label = tk.Label(root, text="Введите название:")
qr_save_name_label.grid(row=3, column=0, padx=10, pady=10)

qr_save_name_entry = tk.Entry(root)
qr_save_name_entry.grid(row=3, column=1, padx=10, pady=10)

version_label = tk.Label(root, text="Версия QR кода:")
version_label.grid(row=4, column=0, padx=10, pady=10)

version_combobox = ttk.Combobox(root, values=[str(i) for i in range(1, 41)], state="readonly")
version_combobox.current(0)
version_combobox.grid(row=4, column=1, padx=10, pady=10)

ext_label = tk.Label(root, text="Расширение:")
ext_label.grid(row=7, column=0, padx=10, pady=10)

ext_combobox = ttk.Combobox(root, values=[".png", ".gif"], state="readonly")
ext_combobox.current(0)
ext_combobox.grid(row=7, column=1, padx=10, pady=10)

contrast_label = tk.Label(root, text="Контраст:")
contrast_label.grid(row=5, column=0, padx=10, pady=10)

contrast_entry = tk.Entry(root)
contrast_entry.insert(0, "1.0")
contrast_entry.grid(row=5, column=1, padx=10, pady=10)

brightness_label = tk.Label(root, text="Яркость:")
brightness_label.grid(row=6, column=0, padx=10, pady=10)

brightness_entry = tk.Entry(root)
brightness_entry.insert(0, "1.0")
brightness_entry.grid(row=6, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Создать QR ", command=generate_qr_code)
generate_button.grid(row=8, column=0, columnspan=3, padx=6, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()