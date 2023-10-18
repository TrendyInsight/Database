-- Buat database jika belum ada
CREATE DATABASE IF NOT EXISTS fashion;
USE fashion;

-- Table Gambar
CREATE TABLE IF NOT EXISTS gambar (
    id_gambar INTEGER PRIMARY KEY AUTO_INCREMENT,
    path_gambar VARCHAR(250)
);

-- Table Jenis
CREATE TABLE IF NOT EXISTS jenis (
    id_jenis INTEGER PRIMARY KEY AUTO_INCREMENT,
    atasan VARCHAR(20),
    bawahan VARCHAR(20),
	terusan VARCHAR(20),
);

-- Table Outfit
CREATE TABLE IF NOT EXISTS outfit (
    id_outfit INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_jenis INTEGER,
    id_gambar INTEGER,
    nama_obyek VARCHAR(50),
    rating VARCHAR(20),
    alasan VARCHAR(100),
    tanggal DATE(),
    jam TIMESTAMP(6),
    FOREIGN KEY (id_jenis) REFERENCES jenis (id_jenis),
        FOREIGN KEY (id_gambar) REFERENCES gambar (id_gambar)
);