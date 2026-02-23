class Vehicle:
    def __init__(self, jenis, merk, tahun_rilis):
        self.jenis = jenis
        self.merk = merk
        self.tahun_rilis = tahun_rilis

    def sound(self):
        print ("suara")
        
class Mobil(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, jumlah_pintu):
        super().__init__(jenis, merk, tahun_rilis)
        self.__jumlah_pintu = jumlah_pintu


    def get_jumlah_pintu(self):
        return self.__jumlah_pintu

class Motor(Vehicle):
    def __init__(self, jenis, merk, tahun_rilis, jumlah_pintu):
        super().__init__(jenis, merk, tahun_rilis)
        self.__jumlah_pintu = jumlah_pintu


    def get_jumlah_pintu(self):
        return self.__jumlah_pintu

v1 = Vehicle("beat", "honda", 2000)
v1.sound()

v2 = Mobil("beat", "honda", 2000, 4)
print(v2.get_jumlah_pintu())

v3 = Motor("beat", "honda", 2000, 2)
print(v3.get_jumlah_pintu())

    



            
            
        