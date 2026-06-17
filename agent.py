from langchain_ollama import ChatOllama
from langchain.tools import tool

# ===================================
# TOOLS
# ===================================

@tool
def calculator(expression: str) -> str:
    """Calculate math expressions."""
    try:
        return str(eval(expression))
    except Exception as e:
        return str(e)

@tool
def knowledge_search(query: str) -> str:
    """Simple search tool."""

    knowledge = {
        "python": "Python is a programming language.",
        "langchain": "LangChain helps build LLM apps.",
        "langgraph": "LangGraph builds AI agent workflows."
    }

    query = query.lower()

    for key, value in knowledge.items():
        if key in query:
            return value

    return "No information found."

# ===================================
# MODEL
# ===================================

llm = ChatOllama(
    model="llama3"
)

# ===================================
# CHAT LOOP
# ===================================

print("AI Agent Started")
print("Type exit to quit")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    if any(x in user for x in ["+", "-", "*", "/"]):
        result = calculator.invoke(user)
        print("Agent:", result)
        continue

    if "python" in user.lower():
        result = knowledge_search.invoke(user)
        print("Agent:", result)
        continue

    response = llm.invoke(user)

    print("Agent:", response.content)