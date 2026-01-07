import dotenv
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile", temperature=0.9)

if __name__ == "__main__":
    result = llm.invoke("Main ingredients in samosa")
    print(result.content)