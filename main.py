from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from graph.builder import build_graph
from tools.price_list import price_list
from tools.term_and_condition import term_and_condition
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Init LLM
llm = init_chat_model("openai:gpt-4o", temperature=0)

# Bind tools to LLM
llm_with_tools = llm.bind_tools([price_list, term_and_condition])

graph = build_graph(llm_with_tools)


# --- Request Models ---
class ChatRequest(BaseModel):
    message: str
    thread_id: str = "default-thread"

# --- Response Models ---
class ChatResponse(BaseModel):
    answer: str


# Init FastAPI
app = FastAPI(title="Jasa Sewa Rote Chatbot API")

origins = [
    "https://www.jasasewarote.web.id",
    'http://localhost:5500',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- API Endpoint ---
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    config = {"configurable": {"thread_id": req.thread_id}}

    state = graph.invoke(
        {"messages": [{"role": "user", "content": req.message}]},
        config=config
    )

    answer = state["messages"][-1].content
    return ChatResponse(answer=answer)
