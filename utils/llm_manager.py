from utils.config import settings
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from functools import lru_cache

@lru_cache(maxsize=5)
def get_llm(model: str, temperature: float , format:str = None):

    # Check if it's an OpenAI model
    if model.startswith("gpt-"):
        return ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model=model,
            temperature=temperature,
            model_kwargs={"response_format": {"type": "json_object"}} if format == "json" else {}
        )

    if settings.USE_LOCAL:
        return ChatOllama(model=model,
                    temperature=temperature,
                    format=format)
    else:
        groq_model = _map_model_to_groq(model)
        return ChatGroq(api_key=settings.GROQ_API_KEY,
                       model=groq_model,
                       temperature=temperature)

def _map_model_to_groq(model: str) -> str:
    """Map Ollama model names to Groq model names."""
    model_mapping = {
        "llama3.1": "llama-3.3-70b-versatile",  # Updated: llama-3.1-70b-versatile was decommissioned
        "llama3": "llama-3.3-70b-versatile",
        "llama2": "llama-2-70b-4096",
        "mixtral": "mixtral-8x7b-32768",
    }
    return model_mapping.get(model, model)


