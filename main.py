from tkinter import *
from tkinter import filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
import qrcode

root = ttk.Window(themename="litera")
root.title("QR Code Generator")
root.geometry("800x650")

def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr.png")

    img_qr = Image.open("qr.png")
    img_qr = img_qr.resize((400, 400))
    tk_img = ImageTk.PhotoImage(img_qr)
    qr_label.config(image=tk_img)
    qr_label.image = tk_img

    btn_guardar.pack(pady=10)

def save_qr():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
        title="Guardar QR como",
    )
    if file_path:
        img = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        img.add_data(entry_data.get())
        img.make(fit=True)
        qr_image = img.make_image(fill_color="black", back_color="white")
        qr_image.save(file_path)

entry_data = ttk.Entry(root, width=40, bootstyle="info")
entry_data.pack(pady=20)

btn_generar = ttk.Button(root, text="Generar QR", bootstyle="primary", command=lambda: generate_qr(entry_data.get()))
btn_generar.pack(pady=10)

qr_label = ttk.Label(root)
qr_label.pack(pady=10)

btn_guardar = ttk.Button(root, text="Guardar QR", bootstyle="success", command=save_qr)
btn_guardar.pack_forget()

root.mainloop()
