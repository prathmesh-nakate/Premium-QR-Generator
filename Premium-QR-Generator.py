import customtkinter as ctk
from tkinter import filedialog, messagebox
import qrcode
from PIL import Image, ImageTk
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Premium QR Code Generator")
app.geometry("700x750")

logo_path = None

# ---------------------- FUNCTIONS ----------------------

def choose_logo():
    global logo_path

    logo_path = filedialog.askopenfilename(
        title="Select Logo",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
    )

    if logo_path:
        messagebox.showinfo("Logo Added", "Logo selected successfully!")

def generate_qr():

    data = entry.get()

    if data == "":
        messagebox.showerror(
            "Error",
            "Please enter text or URL"
        )
        return

    selected_color = color_option.get()

    # QR generation
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(
        fill_color=selected_color,
        back_color="white"
    ).convert("RGB")

    # Add logo in center
    if logo_path:

        logo = Image.open(logo_path)

        logo_size = 80

        logo = logo.resize((logo_size, logo_size))

        qr_width, qr_height = qr_img.size

        position = (
            (qr_width - logo_size) // 2,
            (qr_height - logo_size) // 2
        )

        qr_img.paste(logo, position)

    # Save QR
    save_path = "generated_qr.png"
    qr_img.save(save_path)

    # Preview QR in app
    preview_img = qr_img.resize((300, 300))

    preview = ImageTk.PhotoImage(preview_img)

    qr_label.configure(image=preview)
    qr_label.image = preview

    messagebox.showinfo(
        "Success",
        "QR Code Generated Successfully!"
    )

# ---------------------- UI ----------------------

title = ctk.CTkLabel(
    app,
    text="Premium QR Generator",
    font=("Arial", 30, "bold")
)

title.pack(pady=20)

entry = ctk.CTkEntry(
    app,
    width=500,
    height=50,
    placeholder_text="Enter Text or URL Here"
)

entry.pack(pady=20)

# Color selection
color_option = ctk.CTkComboBox(
    app,
    values=[
        "black",
        "blue",
        "red",
        "green",
        "purple",
        "orange",
        "brown",
        "pink"
    ],
    width=200
)

color_option.set("black")

color_option.pack(pady=10)

# Logo button
logo_button = ctk.CTkButton(
    app,
    text="Choose Logo",
    command=choose_logo
)

logo_button.pack(pady=10)

# Generate button
generate_button = ctk.CTkButton(
    app,
    text="Generate QR",
    width=200,
    height=50,
    command=generate_qr
)

generate_button.pack(pady=20)

# QR Preview
qr_label = ctk.CTkLabel(app, text="")
qr_label.pack(pady=20)

app.mainloop()