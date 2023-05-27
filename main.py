from apartemen import Apartemen
from rumah import Rumah
from indekos import Indekos
from tkinter import *
from PIL import ImageTk, Image
import os

hunians = []

# Membuat objek Apartemen dan menambahkannya ke daftar hunians
hunians.append(Apartemen("Nelly Joy", 3, 3, "Gym, Tempat Parkir, AC", "apart.png", "Bandung, Jawa Barat"))

# Membuat objek Rumah dan menambahkannya ke daftar hunians
hunians.append(Rumah("Sekar MK", 5, 2, "rumah.jpg", "Jakarta Timur, DKI Jakarta"))

# Membuat objek Indekos dan menambahkannya ke daftar hunians
hunians.append(Indekos("Bp. Romi", "Cahya", "kost.jpg", "Depok, Jawa Barat", "Kasur, lemari, kamar mandi dalam"))

# Membuat objek Rumah dan menambahkannya ke daftar hunians
hunians.append(Rumah("Satria", 1, 4, "rumah 2.png", "Bekasi, Jawa Barat"))

# Mengubah direktori kerja ke direktori yang berisi skrip Python
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def details(index):
    # Membuat jendela pop-up baru
    top = Toplevel()
    top.title("Detail " + hunians[index].get_jenis())
    top.configure(bg="lightblue")

    d_frame = LabelFrame(top, text="Data Residen", padx=10, pady=10)
    d_frame.pack(padx=10, pady=10)
    d_frame.configure(bg="lightblue")

    # Menambahkan gambar ke halaman detail
    image = Image.open("assets/" +  hunians[index].get_image())
    image = image.resize((200, 200), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_label = Label(d_frame, image=photo)
    image_label.image = photo
    image_label.pack()

    d_summary = Label(d_frame, text="Summary :\n" + hunians[index].get_detail() + hunians[index].get_fasilitas() + hunians[index].get_summary() + "\n" + hunians[index].get_dokumen(), anchor="w", justify=LEFT)
    d_summary.pack()
    d_summary.configure(bg="lightblue")

    b_close = Button(top, text="Close", command=top.destroy, bg="#E14545")
    b_close.pack(pady=10)


def open_praktikum_page():
    landing_page.withdraw()  # Menyembunyikan jendela landing page
    praktikum_page = Toplevel()
    praktikum_page.configure(bg="lightblue")
    praktikum_page.title("Praktikum DPBO Python")
    
    def back_to_landing():
        praktikum_page.destroy()  # Menutup jendela praktikum page
        landing_page.deiconify()  # Mengembalikan tampilan jendela landing page
    
    frame = LabelFrame(praktikum_page, text="Data Seluruh Residen", padx=10, pady=10)
    frame.pack(padx=10, pady=10)
    frame.configure(bg="lightblue")

    opts = LabelFrame(praktikum_page, padx=10, pady=10)
    opts.pack(padx=10, pady=10)
    opts.configure(bg="lightblue")

    b_add = Button(opts, text="Add Data", state="disabled")
    b_add.grid(row=0, column=0)

    b_exit = Button(opts, text="Exit", command=praktikum_page.destroy)
    b_exit.grid(row=0, column=1)

    for index, h in enumerate(hunians):
        idx = Label(frame, text=str(index+1), width=5, borderwidth=1, relief="solid")
        idx.grid(row=index, column=0)

        type = Label(frame, text=h.get_jenis(), width=15, borderwidth=1, relief="solid")
        type.grid(row=index, column=1)

        if h.get_jenis() != "Indekos": 
            name = Label(frame, text=" " + h.get_nama_pemilik(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)
        else:
            name = Label(frame, text=" " + h.get_nama_penghuni(), width=40, borderwidth=1, relief="solid", anchor="w")
            name.grid(row=index, column=2)

        b_detail = Button(frame, text="Details", command=lambda index=index: details(index), bg="#4DFCA8")
        b_detail.grid(row=index, column=3)

    back_button = Button(praktikum_page, text="Back to Landing Page", command=back_to_landing)
    back_button.pack(pady=10)


landing_page = Tk()
landing_page.title("Landing Page")
landing_page.configure(bg="lightblue")

# Menambahkan gambar ke halaman landing
image = Image.open("assets/bg.png")
image = image.resize((400, 300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
image_label = Label(landing_page, image=photo)
image_label.pack()

text_frame = Frame(landing_page)
text_frame.pack(pady=10)

# Menambahkan teks "Welcome to the Landing Page" di dalam frame
title_label = Label(text_frame, text="Welcome to the Landing Page", font=("Arial", 20), bg="lightblue")
title_label.pack()

enter_button = Button(landing_page, text="Selengkapnya", command=open_praktikum_page, bg="#4DFCA8")
enter_button.pack(pady=10)

landing_page.mainloop()
