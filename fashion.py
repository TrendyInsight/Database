import json
import sqlite3

class FashionApp:
    def __init__(self):
        self.conn = sqlite3.connect("fashion.db")
        self.cursor = self.conn.cursor()
        self.create_tables()  # Panggil fungsi ini untuk membuat tabel jika belum ada

    def create_tables(self):
        with open('fashion.sql', 'r') as sqlfile:  # Pastikan nama file dan pathnya sesuai
            sqlscript = sqlfile.read()
        self.cursor.executescript(sqlscript)
        self.conn.commit()  # Simpan perubahan ke database

    def save_gambar(self, id_gambar, path_gambar): 
        try: 
            self.cursor.execute
            ("INSERT INTO rekomendasi (id_gambar, path_gambar) VALUES (?, ?)", 
             (id_gambar, path_gambar)
            )
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False

    def save_jenis(self, id_jenis, atasan, bawahan, terusan): 
        try: 
            self.cursor.execute
            ("INSERT INTO jenis_baju (id_jenis, atasan, bawahan, terusan) VALUES (?, ?, ?, ?)", 
             (id_jenis, atasan, bawahan, terusan)
            )
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False


    def save_outfit(self, id_outfit, id_jenis, id_gambar, nama_obyek, rating, alasan, tanggal, jam): 
        try: 
            self.cursor.execute
            ("INSERT INTO outfit (id_outfit, id_jenis, id_gambar, nama_obyek, rating, alasan, tanggal, jam) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
             (id_outfit, id_jenis, id_gambar, nama_obyek, rating, alasan, tanggal, jam)
            )
            self.conn.commit()
            return True
        except Exception as e : 
            print("Error:", str(e))
            return False
