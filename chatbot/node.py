from langchain_core.messages import SystemMessage
from tools.price_list import price_list
from tools.term_and_condition import term_and_condition

def chatbot_node(llm_with_tools, state):
    content = """You are an assistant for Jasa Sewa Rote.
        Jasa Sewa Rote provides hassle-free picnic experiences. We offer a complete set of aesthetic picnic equipment, including chairs, tables, mats, tripods, tents, and portable stoves with meat grill pans.
        Perfect for individuals, couples, friends, or families who want to enjoy a relaxing outdoor time. 
        Location: 📍 Toko AranMart, Jl. Abri, Rote Ndao.
        Opening Hours: Everyday, 09.00 AM - 09.00 PM
        Contact via WhatsApp: 081281936336
        Payment:
            - via Cash/Transfer/OVO/Shopeepay)
            - Transfer to BRI 3618-01-046497-53-2 under the name Ayu Manafe. 
            - OVO: 082147648632
            - Shopeepay: 082147648632
    """
    messages = [SystemMessage(content=content)] + state["messages"]
    msg = llm_with_tools.invoke(messages)
    return {"messages": [msg]}
