from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, image, alamat):
        super().__init__(image, alamat, "", "Rumah", jml_penghuni, jml_kamar)
        self.nama_pemilik = nama_pemilik

    # Mengembalikan informasi dokumen terkait rumah, yaitu Izin Mendirikan Bangunan (IMB) atas nama pemilik
    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    # Mengembalikan nilai nama pemilik rumah
    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    # Mengembalikan detail informasi tentang rumah, mencantumkan nama pemilik, jumlah kamar, dan alamat rumah
    def get_detail(self):
        return "Pemilik: " + self.nama_pemilik + "\nJumlah Kamar: " + str(self.jml_kamar) + "\nAlamat: " + str(self.alamat) + "\n"
    
    # Rumah tidak memiliki informasi fasilitas, sehingga mengembalikan nilai kosong
    def get_fasilitas(self):
        return ""
