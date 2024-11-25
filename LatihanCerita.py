import random
import os

class CeritaTokoBangunan:
    def _init_(self):
        self.cat_dinding = ["Nippon paint", "Dulux", "Avitex"]
        self.lakban = ["Horici Tape", "Lucky Tape"]
        self.atap = ["Alderon", "SMARTRUSS", "Taso"]

    def buat_cerita(self):
        random_cat_dinding = random.choice(self.cat_dinding)
        random_lakban = random.choice(self.lakban)
        random_atap = random.choice(self.atap)

        os.system("cls" if os.name == "nt" else "clear")

        print(
            f"Saya membeli barang di toko bangunan. di bintang selatan "
            f"Saya memilih lakban terbaik bermerek {random_lakban} dan membeli cat bermerek {random_cat_dinding}. "
            f"Saya juga membeli atap bermerek {random_atap}. yang digunakan untuk membuat kandang anjing."
        )

def main():
    cerita = CeritaTokoBangunan()
    cerita.buat_cerita()

if __name__ == "_main_":
    main()