from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from typing import Annotated, List, Dict
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.tools import tool
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver


class State(TypedDict):
    messages: Annotated[list, add_messages]


@tool
def term_and_condition():
    """ Return term and condition """
    return [
        {
            "Durasi sewa maksimal 24 jam",
            "Pengembalian max telat 30menit dengan syarat sudah di konfirmasi terlebih dahulu, overtime denda 5.000 rupiah per jam"
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

@tool
def price_list() -> List[Dict]:
    """Return a list of premium quality picnic supplies at prices as cheap as a smile!"""
    return [
        {
            "package_name": "PAKET COUPLE",
            "subtitle": "Sewa Berdua",
            "options": [
                {
                    "item": "Hemat",
                    "item_details": "(2 kursi + 1 meja lipat)",
                    "price": "Rp 40.000",
                },
                {
                    "item": "Komplit",
                    "item_details": "(2 kursi + 1 meja lipat + 1 tripod)",
                    "price": "Rp 55.000",
                },
                {
                    "item": "Sultan",
                    "item_details": "(2 kursi + 1 meja lipat + 1 tripod + 2 topi/kacamata)",
                    "price": "Rp 65.000",
                }
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
                {"item": "Tenda & Matras", "item_details": "", "price": "Rp 50.000"},
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


tools = [price_list, term_and_condition]

llm = init_chat_model("openai:gpt-4o", temperature=0)
llm_with_tools = llm.bind_tools(tools)

def chatbot_node(state: State):
    content = """You are an assistant for Jasa Sewa Rote.
        Jasa Sewa Rote provides hassle-free picnic experiences. We offer a complete set of aesthetic picnic equipment, including chairs, tables, mats, tripods, tents, and portable stoves with meat grill pans.
        Perfect for individuals, couples, friends, or families who want to enjoy a relaxing outdoor time. 
        Location: 📍 Toko AranMart, Jl. Abri, Rote Ndao.
        Opening Hours: Everyday, 09.00 AM - 09.00 PM
        Payment:
            - via Cash/Transfer/OVO/Shopeepay)
            - Transfer to BRI 3618-01-046497-53-2 under the name Ayu Manafe. 
            - OVO: 082147648632
            - Shopeepay: 082147648632
    """
    messages = [
        SystemMessage(content= content),
    ] + state["messages"]
    msg = llm_with_tools.invoke(messages)
    return {"messages": [msg]}

memory = MemorySaver()
builder = StateGraph(State)
builder.add_node("chatbot", chatbot_node)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "chatbot")
builder.add_conditional_edges("chatbot", tools_condition)
builder.add_edge("tools", "chatbot")
builder.add_edge("chatbot", END)
graph = builder.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "thread-yugjhb988-9098nku"}}

query="kalau sewa tripod harga nya berapa?"

state = graph.invoke({"messages": [{"role": "user", "content": query}]}, config=config)
print(state["messages"][-1].content)


# if __name__ == '__main__':
