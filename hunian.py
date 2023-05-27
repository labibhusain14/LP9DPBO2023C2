class Hunian():
    def __init__(self, image, alamat, fasilitas, jenis, jml_penghuni=1, jml_kamar=1):
        self.image = image  # Menyimpan nilai gambar hunian
        self.alamat = alamat  # Menyimpan alamat hunian
        self.fasilitas = fasilitas  # Menyimpan fasilitas yang tersedia di hunian
        self.jenis = jenis  # Menyimpan jenis hunian (Apartemen, Rumah, Indekos, dll)
        self.jml_penghuni = jml_penghuni  # Menyimpan jumlah penghuni yang tinggal di hunian (default: 1)
        self.jml_kamar = jml_kamar  # Menyimpan jumlah kamar yang tersedia di hunian (default: 1)

    def get_image(self):
        return self.image  # Mengembalikan nilai gambar hunian
    
    def get_alamat(self):
        return self.alamat  # Mengembalikan nilai alamat hunian
    
    def get_jenis(self):
        return self.jenis  # Mengembalikan nilai jenis hunian

    def get_jml_penghuni(self):
        return self.jml_penghuni  # Mengembalikan nilai jumlah penghuni hunian

    def get_jml_kamar(self):
        return self.jml_kamar  # Mengembalikan nilai jumlah kamar hunian

    def get_dokumen(self):
        pass  # Metode ini belum diimplementasikan, bisa digunakan untuk mengambil informasi dokumen terkait hunian

    def get_fasilitas(self):
        pass  # Metode ini belum diimplementasikan, bisa digunakan untuk mengambil informasi fasilitas hunian
    
    def get_summary(self):
        return "Hunian " + self.jenis + ", ditempati oleh " + str(self.jml_penghuni) + " orang."
        # Mengembalikan ringkasan informasi tentang hunian, mencantumkan jenis dan jumlah penghuni
