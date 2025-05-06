# Kalimat pembuka
print("Halo calon mahasiswa/i IT baru!\n")

# Daftar Perguruan Tinggi Negri/Swasta
kampus_list = {
    "PTN": [
        {"nama": "Universitas Indonesia", "minimal_nem": 95},
        {"nama": "Institut Teknologi Bandung", "minimal_nem": 90},
        {"nama": "Universitas Gajah Mada", "minimal_nem": 85},
        {"nama": "Universitas Pendidikan Indonesia", "minimal_nem": 75},
    ],
    "PTS": [
        {"nama": "Telkom University", "minimal_nem": 85},
        {"nama": "Universitas Bina Nusantara", "minimal_nem": 80},
        {"nama": "Universitas Kristen Petra", "minimal_nem": 75},
    ]
}

# Input data
nama = input("Masukkan nama: ")
nem = float(input("Masukkan NEM : "))
perguruan_tinggi = input("Perguruan tinggi yang diinginkan (PTN/PTS): ").upper()

# Filter dan tampilkan rekomendasi kampus
print(f"\nRekomendasi Perguruan Tinggi untuk {nama} di {perguruan_tinggi}:")
found = False
for kampus in kampus_list.get(perguruan_tinggi, []):
    if nem >= kampus["minimal_nem"]:
        print(f"- {kampus['nama']}")
        found = True

# Jika NEM tidak masuk ke dalam katagori
if not found:
    print(F"Mohon maaf, belum ada Perguruan Tinggi yang cocok untuk {nama}.\n")
    pilihan = input("Apakah kamu tertarik mengikuti short course IT?\n(ya/tidak): ").lower()
    
    if pilihan == "ya":
        print("\nKami rekomendasikan mendaftar short course di https://codingstudio.id untuk meningkatkan kemampuanmu.")

    else:
         print("\nTerima kasih!")
