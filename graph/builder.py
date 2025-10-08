from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver

from tools.price_list import price_list
from tools.term_and_condition import term_and_condition
from chatbot.node import chatbot_node

class State(TypedDict):
    messages: Annotated[list, add_messages]

def build_graph(llm_with_tools):
    memory = MemorySaver()
    builder = StateGraph(State)
    builder.add_node("chatbot", lambda state: chatbot_node(llm_with_tools, state))
    builder.add_node("tools", ToolNode([price_list, term_and_condition]))
    builder.add_edge(START, "chatbot")
    builder.add_conditional_edges("chatbot", tools_condition)
    builder.add_edge("tools", "chatbot")
    builder.add_edge("chatbot", END)
    return builder.compile(checkpointer=memory)
