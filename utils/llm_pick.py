from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def pick_llm(level: str):
    if level.lower() in ["low", "medium", "high", "claude"]:
        return ChatGoogleGenerativeAI(
            model="gemini-3.5-flash-lite",
            temperature=0
        )
    else:
        raise ValueError(f"Unsupported level: {level}")


if __name__ == "__main__":
    llm_obj = pick_llm("low")
    response = llm_obj.invoke("What is the capital of France?")
    print(response.content)