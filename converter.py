import pycdlib
import tkinter as tk
from tkinter import filedialog, messagebox
import shutil

def convert_img_to_iso(img_path, iso_path):
    shutil.copyfile(img_path, iso_path)

def select_img_file():
    img_path = filedialog.askopenfilename(
        title="Select .img file",
        filetypes=[("IMG files", "*.img")]
    )
    if img_path:
        save_iso_file(img_path)

def save_iso_file(img_path):
    iso_path = filedialog.asksaveasfilename(
        title="Save as .iso file",
        defaultextension=".iso",
        filetypes=[("ISO files", "*.iso")]
    )
    if iso_path:
        try:
            convert_img_to_iso(img_path, iso_path)
            messagebox.showinfo("Success", f"Converted {img_path} to {iso_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert: {str(e)}")

root = tk.Tk()
root.title("IMG to ISO Converter")
root.geometry("300x150")

convert_button = tk.Button(root, text="Select .img file to convert", command=select_img_file)
convert_button.pack(pady=20)

root.mainloop()