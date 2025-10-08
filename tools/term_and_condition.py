from langchain_core.tools import tool

@tool
def term_and_condition():
    """Return term and condition"""
    return [
        {
            "Durasi sewa maksimal 24 jam",
            "Pengembalian max telat 30 menit dengan syarat sudah di konfirmasi terlebih dahulu, overtime denda 5.000 rupiah per jam"
        },
        {
            "Wajib meninggalkan identitas diri & nomor telepon aktif",
            "KTP/SIM/KTM/Kartu Pelajar yang masih aktif (akan di kembalikan setelah barang sewa di kembalikan sesuai S&K yang berlaku)"
        },
        {
            "Barang kembali dalam keadaan awal disewa",
            "Tidak basah, tidak noda, tidak cacat, tidak rusak. Jagalah kebersihkan barang selayaknya barang milik pribadi"
        },
        {
            "Kerusakan atau Kehilangan barang menjadi tanggung jawab penyewa",
            "Kerusakan atau kehilangan unit akan di kenakan denda perbarang sesuai harga beli di pasaran"
        },
        {
            "Pembayaran di awal (pembayaran via Cash/TF/OVO/Shopeepay)",
            "TF BRI 3618-01-046497-53-2 a/n Ayu Manafe. OVO/Shopeepay 082147648632"
        },
        "Menyewa = Menyetujui S&K yang berlaku‼️"
    ]
