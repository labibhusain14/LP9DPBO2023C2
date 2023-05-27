from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, image, alamat, fasilitas):
        super().__init__(image, alamat, fasilitas, "Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni

    # Mengembalikan informasi dokumen terkait indekos, yaitu bukti kontrak indekos antara penghuni dengan pemilik
    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    # Mengembalikan nilai nama pemilik indekos
    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    # Mengembalikan nilai nama penghuni indekos
    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    # Mengembalikan ringkasan informasi tentang indekos
    def get_summary(self):
        return "Hunian Indekos."
    
    # Mengembalikan detail informasi tentang indekos, mencantumkan nama pemilik, alamat kost, dan nama penghuni
    def get_detail(self):
        return "Pemilik: " + self.nama_pemilik + "\nAlamat kost: " + str(self.alamat) + "\nPenghuni kost: " + str(self.nama_penghuni) + "\n"
    
    # Mengembalikan informasi fasilitas yang tersedia di indekos
    def get_fasilitas(self):
        return "Fasilitas: " + self.fasilitas + "\n"
