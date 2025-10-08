from typing import List, Dict
from langchain_core.tools import tool

@tool
def price_list() -> List[Dict]:
    """Return a list of premium quality picnic supplies at prices as cheap as a smile!"""
    return [
        {
            "package_name": "PAKET COUPLE",
            "subtitle": "Sewa Berdua",
            "options": [
                {"item": "Hemat", "item_details": "(2 kursi + 1 meja lipat)", "price": "Rp 40.000"},
                {"item": "Komplit", "item_details": "(2 kursi + 1 meja lipat + 1 tripod)", "price": "Rp 55.000"},
                {"item": "Sultan", "item_details": "(2 kursi + 1 meja lipat + 1 tripod + 2 topi/kacamata)", "price": "Rp 65.000"},
            ]
        },
        {
            "package_name": "PAKET JOMBLO",
            "subtitle": "Sewa Satuan",
            "options": [
                {"item": "Kacamata", "item_details": "", "price": "Rp 10.000"},
                {"item": "Topi pantai/bucket hat", "item_details": "", "price": "Rp 10.000"},
                {"item": "Kursi lipat", "item_details": "", "price": "Rp 15.000"},
                {"item": "Meja lipat", "item_details": "", "price": "Rp 15.000"},
                {"item": "Tikar Aesthetic", "item_details": "", "price": "Rp 15.000"},
                {"item": "Kursi Lipat Sultan", "item_details": "", "price": "Rp 20.000"},
                {"item": "Tripod + remote bluetooth", "item_details": "", "price": "Rp 20.000"},
                {"item": "Kompor Portable", "item_details": "", "price": "Rp 25.000"},
                {"item": "Tenda & Matras", "item_details": "", "price": "Rp 80.000"},
                {"item": "Sleeping Bag", "item_details": "", "price": "Rp 50.000"}
            ]
        },
        {
            "package_name": "PAKET BESTIE",
            "subtitle": "Sewa Kelompok",
            "options": [
                {"item": "Kenyang", "item_details": "(1 kompor + 1 pan anti lengket + capitan & kuas)", "price": "Rp 45.000"},
                {"item": "Senang", "item_details": "(1 kompor + 1 pan anti lengket + capitan & kuas + 1 Tikar aesthetic)", "price": "Rp 55.000"},
                {"item": "Bahagia", "item_details": "(1 kompor + 1 pan anti lengket + capitan & kuas + 1 Tikar aesthetic + 1 tripod)", "price": "Rp 65.000"},
                {"item": "Super Bahagia", "item_details": "(1 kompor + 1 pan anti lengket + capitan & kuas + 1 Tikar aesthetic + 1 tripod + 1 tenda & matras)", "price": "Rp 100.000"},
            ]
        },
    ]
